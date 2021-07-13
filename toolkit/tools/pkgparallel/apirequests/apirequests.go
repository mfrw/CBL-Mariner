package main

import (
    "encoding/json"
    "fmt"
    "log"
    "io/ioutil"
    "net/http"
    "github.com/gorilla/mux"
    "database/sql"
    _ "github.com/go-sql-driver/mysql"
)

type Pkg struct {
    PkgID      	 string    `json:"PkgID"`
    StatusCode   string `json:"StatusCode"`
}

var db *sql.DB
var Pkgs []Pkg

func connect() {
    db, err = sql.Open("mysql", "root:8520@tcp(127.0.0.1:3306)/world")
    if err != nil {
        fmt.Println(err.Error())
    } else {
        fmt.Println("successfully connected to database.")
    }
}

func homePage(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Welcome to the HomePage!")
    fmt.Println("Endpoint Hit: homePage")
}

func returnAllPkgs(w http.ResponseWriter, r *http.Request) {
    fmt.Println("Endpoint Hit: returnAllPkgs")
    json.NewEncoder(w).Encode(Pkgs)
}

func returnSinglePkgs(w http.ResponseWriter, r *http.Request) {
    vars := mux.Vars(r)
    key := vars["id"]

    for _, pkg := range Pkgs {
        if pkg.PkgID == key {
            json.NewEncoder(w).Encode(pkg)
        }
    }
}


func createNewPkg(w http.ResponseWriter, r *http.Request) {   
    reqBody, _ := ioutil.ReadAll(r.Body)
    var pkg Pkg 
    json.Unmarshal(reqBody, &pkg)
    Pkgs = append(Pkgs, pkg)
    json.NewEncoder(w).Encode(pkg)
}

func deletePkg(w http.ResponseWriter, r *http.Request) {
    vars := mux.Vars(r)
    id := vars["id"]

    for index, pkg := range Pkgs {
        if pkg.PkgID == id {
            Pkgs = append(Pkgs[:index], Pkgs[index+1:]...)
        }
    }

}

func updatePkgs(w http.ResponseWriter, r *http.Request) {
	id := mux.Vars(r)["id"]
	var pkg Pkg

	reqBody, err := ioutil.ReadAll(r.Body)
	if err != nil {
		fmt.Fprintf(w, "Kindly enter data with the event title and description only in order to update")
	}
	json.Unmarshal(reqBody, &pkg)

	for i, pack := range Pkgs {
		if pack.PkgID == id {
			pack.StatusCode = pkg.StatusCode
			Pkgs = append(Pkgs[:i], pack)
			json.NewEncoder(w).Encode(pack)
		}
	}
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
        Pkg{PkgID: "1", StatusCode: "Building"},
        Pkg{PkgID: "2", StatusCode: "Built"},
    }
    handleRequests()
}