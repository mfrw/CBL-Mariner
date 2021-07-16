package APIRequests

import (
    "log"
    "encoding/json"
    "io/ioutil"
    "fmt"
    "net/http"
    "github.com/gorilla/mux"
    "time"
    "context"

    "go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
    "go.mongodb.org/mongo-driver/bson/primitive"
)
//Why this driver
// add BSON tag
type Pkg struct {
    PkgID      	 string    `json:"PkgID"`
    StatusCode   string `json:"StatusCode"`
    Location     string `json:"Location"`
}

var Pkgs []Pkg

//MongoDB locally
func connect() (*mongo.Collection, context.Context) {
    client, err := mongo.NewClient(options.Client().ApplyURI())
    if err != nil {
        log.Fatal(err)
    }
    ctx, _ := context.WithTimeout(context.Background(), 10*time.Second)
    err = client.Connect(ctx)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Disconnect(ctx)
    quickstartDatabase := client.Database("mariner")
    pkgCollection := quickstartDatabase.Collection("packages")
    return pkgCollection,ctx
}

func homePage(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Welcome to the HomePage!")
    fmt.Println("Endpoint Hit: homePage")
}

func returnAllPkgs(w http.ResponseWriter, r *http.Request) {
    collection, context := connect()
    cur, _ := collection.Find(context, bson.M{})
    
    for cur.Next(context){
        var pkg Pkg
		// & character returns the memory address of the following variable.
		err := cur.Decode(&pkg) // decode similar to deserialize process.
		if err != nil {
			log.Fatal(err)
		}

		// add item our array
		Pkgs = append(Pkgs, pkg)
    }
    fmt.Println("Endpoint Hit: returnAllPkgs")
    json.NewEncoder(w).Encode(Pkgs)
}

func returnSinglePkgs(w http.ResponseWriter, r *http.Request) {
    var book Pkg
    collection, context := connect()
    _, err := collection.Find(context, bson.M{})
    if (err!=nil){
        fmt.Println("Error")
    }

    var params = mux.Vars(r)
	id, _ := primitive.ObjectIDFromHex(params["id"])

	filter := bson.M{"_id": id}
	err = collection.FindOne(context, filter).Decode(&book)

    vars := mux.Vars(r)
    key := vars["id"]

    for _, pkg := range Pkgs {
        if pkg.PkgID == key {
            json.NewEncoder(w).Encode(pkg)
        }
    }
}


func createNewPkg(w http.ResponseWriter, r *http.Request) {  
    collection, context := connect()
    _, err := collection.Find(context, bson.M{})
    if (err!=nil){
        fmt.Println(err.Error)
    }

    w.Header().Set("Content-Type", "application/json")

	var book Pkg

	// we decode our body request params
	_ = json.NewDecoder(r.Body).Decode(&book)

	// insert our book model.
	result, err := collection.InsertOne(context, book)


	json.NewEncoder(w).Encode(result)
}

func deletePkg(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "application/json")
    collection, context := connect()
    _, err := collection.Find(context, bson.M{})
    if (err!=nil){
        fmt.Println(err.Error)
    }
	// get params
	var params = mux.Vars(r)

	// string to primitve.ObjectID
	id, err := primitive.ObjectIDFromHex(params["id"])

	// prepare filter.
	filter := bson.M{"_id": id}

	deleteResult, err := collection.DeleteOne(context, filter)

	json.NewEncoder(w).Encode(deleteResult)
}

func updatePkgs(w http.ResponseWriter, r *http.Request) {
    collection, context := connect()
    cur, _ := collection.Find(context, bson.M{})
    _=cur
    w.Header().Set("Content-Type", "application/json")

	var params = mux.Vars(r)

	//Get id from parameters
	id, _ := primitive.ObjectIDFromHex(params["id"])

	var book Pkg

	// Create filter
	filter := bson.M{"_id": id}

	// Read update model from body request
	_ = json.NewDecoder(r.Body).Decode(&book)
    update := bson.D{
		{"$set", bson.D{
			{"PkgID", book.PkgID},
			{"StatusCode", book.StatusCode},
			{"Location", book.Location},
        },
    }}

	err1 := collection.FindOneAndUpdate(context, filter, update).Decode(&book)
    if err1 != nil {
        fmt.Println("Error")
    }
    book.PkgID = string(id)

	json.NewEncoder(w).Encode(book)
}

func handleRequests() {
    myRouter := mux.NewRouter().StrictSlash(true)
    myRouter.HandleFunc("/", homePage)
    myRouter.HandleFunc("/packages", returnAllPkgs)
    myRouter.HandleFunc("/pkg", createNewPkg).Methods("POST")
    myRouter.HandleFunc("/pkg/{id}", deletePkg).Methods("DELETE")
    myRouter.HandleFunc("/pkg/{id}", returnSinglePkgs)
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