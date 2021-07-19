package main

import (
    "log"
    "encoding/json"
    // "io/ioutil"
    "fmt"
    "net/http"
    "github.com/gorilla/mux"
    // "time"
    "context"

    "go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
    "go.mongodb.org/mongo-driver/bson/primitive"
)
//Why this driver
// add BSON tag
type Pkg struct {
    PkgID      	 string    `json:"PkgID" bson:"PkgID"`
    StatusCode   string `json:"StatusCode" bson:"StatusCode"`
    Location     string `json:"Location" bson:"Location"`
}

var Pkgs []Pkg

//MongoDB locally
func connect() *mongo.Collection {
    clientOptions := options.Client().ApplyURI("mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb")
    client, err := mongo.Connect(context.TODO(), clientOptions)

	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Connected to MongoDB!")

	collection := client.Database("mariner").Collection("packages")

	return collection
}
type ErrorResponse struct {
	StatusCode   int    `json:"status"`
	ErrorMessage string `json:"message"`
}

func GetError(err error, w http.ResponseWriter) {

	// log.Fatal(err.Error())
	var response = ErrorResponse{
		ErrorMessage: err.Error(),
		StatusCode:   http.StatusInternalServerError,
	}

	message, _ := json.Marshal(response)

	w.WriteHeader(response.StatusCode)
	w.Write(message)
}

func homePage(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Welcome to the HomePage!")
    fmt.Println("Endpoint Hit: homePage")
}

func returnAllPkgs(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "application/json")

	// we created Book array
	var books []Pkg
    collection:=connect()

	// bson.M{},  we passed empty filter. So we want to get all data.
	cur, err := collection.Find(context.TODO(), bson.M{})

	if err != nil {
		fmt.Println(err)
		return
	}

	// Close the cursor once finished
	/*A defer statement defers the execution of a function until the surrounding function returns.
	simply, run cur.Close() process but after cur.Next() finished.*/
	defer cur.Close(context.TODO())

	for cur.Next(context.TODO()) {

		// create a value into which the single document can be decoded
		var book Pkg
		// & character returns the memory address of the following variable.
		err := cur.Decode(&book) // decode similar to deserialize process.
		if err != nil {
			log.Fatal(err)
		}

		// add item our array
		books = append(books, book)
	}

	if err := cur.Err(); err != nil {
		GetError(err, w)
	}

	json.NewEncoder(w).Encode(books)
}

func returnSinglePkgs(w http.ResponseWriter, r *http.Request) {
    var book Pkg
    collection := connect()
    w.Header().Set("Content-Type", "application/json")

	// we get params with mux.
	var params = mux.Vars(r)

	// string to primitive.ObjectID
	PkgID, _ := params["id"]
	// fmt.Println(params, PkgID)

	// We create filter. If it is unnecessary to sort data for you, you can use bson.M{}
	filter := bson.M{"PkgID":PkgID}
	err := collection.FindOne(context.TODO(), filter).Decode(&book)

	if err != nil {
		GetError(err, w)
		return
	}

	json.NewEncoder(w).Encode(book)
}


func createNewPkg(w http.ResponseWriter, r *http.Request) {  
    collection := connect()
    w.Header().Set("Content-Type", "application/json")

	var book Pkg

	// we decode our body request params
	_ = json.NewDecoder(r.Body).Decode(&book)
	fmt.Println(book)

	// insert our book model.
	result, err := collection.InsertOne(context.TODO(), book)

	if err != nil {
		GetError(err, w)
		return
	}

	json.NewEncoder(w).Encode(result)
}

func deletePkg(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "application/json")
    collection:= connect()
    var params = mux.Vars(r)

	// string to primitve.ObjectID
	id, err := primitive.ObjectIDFromHex(params["PkgID"])

	// prepare filter.
	filter := bson.M{"PkgID": id}

	deleteResult, err := collection.DeleteOne(context.TODO(), filter)

	if err != nil {
	    GetError(err, w)
		return
	}
	json.NewEncoder(w).Encode(deleteResult)
}

func updatePkgs(w http.ResponseWriter, r *http.Request) {
    collection := connect()
    w.Header().Set("Content-Type", "application/json")
    var book Pkg

    var params = mux.Vars(r)

	//Get id from parameters
	id, _ := primitive.ObjectIDFromHex(params["PkgID"])


	// Create filter
	filter := bson.M{"PkgID": id}

	// Read update model from body request
	_ = json.NewDecoder(r.Body).Decode(&book)
    update := bson.D{
		{"$set", bson.D{
			{"PkgID", book.PkgID},
			{"StatusCode", book.StatusCode},
			{"Location", book.Location},
        },}}

        err := collection.FindOneAndUpdate(context.TODO(), filter, update).Decode(&book)

        if err != nil {
            GetError(err, w)
            return
        }
    
        book.PkgID = id.Hex()
    
        json.NewEncoder(w).Encode(book)
}

func handleRequests() {
    myRouter := mux.NewRouter().StrictSlash(true)
    myRouter.HandleFunc("/", homePage)
    myRouter.HandleFunc("/packages", returnAllPkgs).Methods("GET")
    myRouter.HandleFunc("/pkg", createNewPkg).Methods("POST")
    myRouter.HandleFunc("/pkg/{id}", deletePkg).Methods("DELETE")
    myRouter.HandleFunc("/pkg/{id}", returnSinglePkgs).Methods("GET")
	myRouter.HandleFunc("/pkg/{id}", updatePkgs).Methods("PATCH")
    log.Fatal(http.ListenAndServe(":10000", myRouter))
}

func main() {
    Pkgs = []Pkg{
        Pkg{PkgID: "1", StatusCode: "Building", Location:"/home/rakshaa/CBL-Mariner/toolkit/tools/pkgparallel/threads/pkgloc/pk1"},
        Pkg{PkgID: "2", StatusCode: "Built", Location:"/home/rakshaa/CBL-Mariner/toolkit/tools/pkgparallel/threads/pkgloc/pk2"},
    }
    handleRequests()
}