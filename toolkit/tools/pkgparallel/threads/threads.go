// Go program to illustrate send
// and receive operation
package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"

	"gonum.org/v1/gonum/graph"
	"microsoft.com/pkggen/internal/pkggraph"
	"microsoft.com/pkggen/pkgparallel/apirequests"
	"microsoft.com/pkggen/pkgparallel/clustering"
)

func Build(ch chan graph.Node) {
	var i graph.Node
	i = <-ch
	client := &http.Client{}
	link:= "https://localhost:10000/pkg/"+string(i.ID())
	req, err := http.NewRequest("GET", link, nil)
	if err != nil {
	fmt.Print(err.Error())
	}
	req.Header.Add("Accept", "application/json")
	req.Header.Add("Content-Type", "application/json")
	resp, err := client.Do(req)
	if err != nil {
	fmt.Print(err.Error())
	}
	defer resp.Body.Close()
	bodyBytes, err := ioutil.ReadAll(resp.Body)
	if err != nil {
	fmt.Print(err.Error())
	}
	var responseObject APIRequests.Pkg
	json.Unmarshal(bodyBytes, &responseObject)
	fmt.Println(<-ch)
}
func main() {
	file := "/home/rakshaa/CBL-Mariner/toolkit/tools/pkgparallel/threads/cdrkit.dot"
	g := pkggraph.NewPkgGraph()
	err := pkggraph.ReadDOTGraphFile(g, file)
	_ = err
	leader := Clusterise.Clusterise(g)
	lists:= make(map[graph.Node][]graph.Node)
	for key, element := range leader{
		lists[element] = append(lists[element],key)
	}
	var q [][]graph.Node
	for _, element := range lists{
		var l []graph.Node
		for _,i := range element{
			l=append(l,i)
		}
		q=append(q,l)
	}
	q0:=q[0]
	q1:=q[1]
	go func() {
		for _,i := range q0{
			var ch chan graph.Node
			ch<-i
			Build(ch)
		}
	}()
	go func() {
		for _,i := range q1{
			var ch chan graph.Node
			ch<-i
			Build(ch)
		}
	}()
}
