package main
import (
	"fmt"
	// "log"
	// "gonum.org/v1/gonum/graph"
	// "microsoft.com/pkggen/internal/logger"
	// "microsoft.com/pkggen/internal/pkggraph"
	// clusterise "microsoft.com/pkggen/pkgparallel/clustering"
	"strconv"
	"encoding/json"
	"net/http"
	"bytes"
	// "crypto/tls"
)
type Pkg struct {
    PkgID      	 string    `json:"PkgID" bson:"PkgID"`
    StatusCode   string `json:"StatusCode" bson:"StatusCode"`
    Location     string `json:"Location" bson:"Location"`
}


func main() {
	// logger.InitBestEffort("/tmp/somelog", "INFO")
	// file := "/home/rakshaa/CBL-Mariner/toolkit/tools/pkgparallel/threads/cdrkit.dot"
	// g := pkggraph.NewPkgGraph()
	// err := pkggraph.ReadDOTGraphFile(g, file)
	// if err != nil {
	// 	log.Fatal(err)
	// }
	// leader:= clusterise.Clusterise(g)
	// lists := make(map[graph.Node][]graph.Node)
	// for key, element := range leader {
	// 	lists[element] = append(lists[element], key)
	// }
	// for _, value := range lists {
	// 	fmt.Println(len(value))
	// }
	// tr := &http.Transport{
    //     TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
    // }
    // client := &http.Client{Transport: tr}
	var post Pkg
	str := strconv.Itoa(int(4))
	link := "http://localhost:10000/pkg"
	_=link
	post.PkgID = str
	post.StatusCode = "Starting"
	post.Location = "/home/rakshaa/CBL-Mariner/toolkit/tools/pkgparallel/threads/pkgloc/"+ str
	j,_:=json.Marshal(map[string]string{
		"PkgID": post.PkgID,
		"StatusCode":post.StatusCode,
		"Location":post.Location,
	}) 
	
    resp, err := http.Post(link, "application/json", bytes.NewBuffer(j))

    if err != nil {
        fmt.Println(err)
    }

    var res map[string]interface{}

    json.NewDecoder(resp.Body).Decode(&res)

    fmt.Println(res)
	// defer req.Body.Close()
}