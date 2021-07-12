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
func CheckBuild(g *pkggraph.PkgGraph, i graph.Node) bool{
	dep:=graph.NodesOf(g.From(i.ID()))
	client := &http.Client{}
	for _, node := range dep{
		id:=node.ID()
		link:="https://localhost:10000/pkg/"+id
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
		var responseObject APIResponse.Pkg
		json.Unmarshal(bodyBytes, &responseObject)
		if responseObject.StatusCode!="Built"{
			var post APIResponse.Pkg
			link:="https://localhost:10000/pkg/"+i.ID()
			post.ID = i.ID()
			post.StatusCode = "Queued"
			req, err := http.PostForm(link, post)
			return false
		}
	}
	var post APIResponse.Pkg
	link:="https://localhost:10000/pkg/"+i.ID()
	post.ID = i.ID()
	post.StatusCode = "Building"
	req, err := http.PostForm(link, post)
	return true
}
func Build(ch chan graph.Node) {
	var i graph.Node
	i = <-ch
	fmt.Println(<-ch)
	var post APIResponse.Pkg
	link:="https://localhost:10000/pkg/"+i.ID()
	post.ID = i.ID()
	post.StatusCode = "Built"
	req, err := http.PostForm(link, post)
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
