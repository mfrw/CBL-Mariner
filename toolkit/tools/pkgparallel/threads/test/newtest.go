package main

import (
	"fmt"
	"log"
	"gonum.org/v1/gonum/graph"
	"microsoft.com/pkggen/internal/logger"
	"microsoft.com/pkggen/internal/pkggraph"
	clusterise "microsoft.com/pkggen/pkgparallel/clustering"
	// "bytes"
	// "encoding/json"
	// "net/http"
	// "strconv"
	// "os/exec"
	// "os"
	// "crypto/tls"
)
type Pkg struct {
    PkgID      	 string    `json:"PkgID" bson:"PkgID"`
    StatusCode   string `json:"StatusCode" bson:"StatusCode"`
    Location     string `json:"Location" bson:"Location"`
}


func main() {
	// for i:=0;i<4; i++{
	// 	cmd:= exec.Command("sh","-c","cd ~")
	// 	out, err1:=cmd.CombinedOutput()
	// 	fmt.Println(string(out))
	// 	if err1 != nil {
	// 		fmt.Println(err1)
	// 	} else{
	// 		fmt.Println("For loop")
	// 		cmd = exec.Command("sh", "-c","echo stdout; pwd")
	// 		out,_=cmd.CombinedOutput()
	// 		fmt.Println(string(out))
	// 	}
	// }
	// os.Chdir("/home/rakshaa/CBL-Mariner/toolkit")
	// command:= "REBUILD_TOOLS=y"
	// cmd := exec.Command("sudo", "make", "toolchain", command)
	// out, err := cmd.Output()

	// cmd.Stderr = os.Stderr
	// cmd.Stdin = os.Stdin
	// out, err := cmd.Output()
	// command:= "SPECS_DIR=/home/rakshaa/CBL-Mariner/build/INTERMEDIATE_SPECS/ipxe-1.20.1-3.cm1"
	// cmd := exec.Command("sudo", "make", "build-packages", command)
	// cmd.Stderr = os.Stderr
	// cmd.Stdin = os.Stdin

	// out, err := cmd.Output()
	// if err != nil {
	// 	fmt.Println("Err", err)
	// } else {
	// 	fmt.Println("OUT:", string(out))
	// }
	
	logger.InitBestEffort("/tmp/somelog", "INFO")
	file := "/home/rakshaa/CBL-Mariner/toolkit/tools/pkgparallel/files/reverse-cdrkit.dot"
	g := pkggraph.NewPkgGraph()
	err := pkggraph.ReadDOTGraphFile(g, file)
	if err != nil {
		log.Fatal(err)
	}
	// fmt.Println(graph.NodesOf(g.From(2)))
	leader:= clusterise.Clusterise(g)
	fmt.Println(leader[15])
	lists := make(map[graph.Node][]graph.Node)
	for key, element := range leader {
		lists[element] = append(lists[element], key)
	}
	for _, value := range lists {
		fmt.Println(len(value))
		// fmt.Println(value)
	}
	// tr := &http.Transport{
    //     TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
    // }
    // client := &http.Client{}
	// var post Pkg
	// str := strconv.Itoa(int(1))
	// link := "http://localhost:10000/pkg/1"
	// _=link
	// post.PkgID = str
	// post.StatusCode = "Queued"
	// post.Location = "/home/rakshaa/CBL-Mariner/build/INTERMEDIATE_SPECS/bash-4.4.18-6.cm1/bash.spec"
	// j,_:=json.Marshal(map[string]string{
	// 	"PkgID": post.PkgID,
	// 	"StatusCode":post.StatusCode,
	// 	"Location":post.Location,
	// }) 
	
    // req, err := http.NewRequest("PATCH", link, bytes.NewBuffer(j))

    // if err != nil {
    //     fmt.Println(err)
    // }
	// resp, _:=client.Do(req)
	// fmt.Println(resp)
    // var res map[string]interface{}

    // json.NewDecoder(resp.Body).Decode(&res)

    // fmt.Println(res)
	// defer req.Body.Close()
}