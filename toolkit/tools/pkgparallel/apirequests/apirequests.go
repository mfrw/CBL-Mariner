package apirequests

import (
    "encoding/json"
    "fmt"
    "log"
    "io/ioutil"
    "net/http"
    "github.com/gorilla/mux"
)

// Article - Our struct for all articles
type Pkg struct {
    PkgID      	 string    `json:"PkgID"`
    StatusCode   string `json:"StatusCode"`
}

var Pkgs []Pkg

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