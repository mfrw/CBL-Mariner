// Go program to illustrate send
// and receive operation
package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"net/url"

	"gonum.org/v1/gonum/graph"
	"microsoft.com/pkggen/internal/logger"
	"microsoft.com/pkggen/internal/pkggraph"

	// "microsoft.com/pkggen/pkgparallel/apirequests"
	Clusterise "microsoft.com/pkggen/pkgparallel/clustering"
)

type Pkg struct {
	PkgID      string `json:"PkgID"`
	StatusCode string `json:"StatusCode"`
}

func CheckBuild(g *pkggraph.PkgGraph, i graph.Node) bool {
	dep := graph.NodesOf(g.From(i.ID()))
	client := &http.Client{}
	for _, node := range dep {
		id := node.ID()
		link := "https://localhost:10000/pkg/" + string(id)
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
		var responseObject Pkg
		json.Unmarshal(bodyBytes, &responseObject)
		if responseObject.StatusCode != "Built" {
			var post Pkg
			link := "https://localhost:10000/pkg/" + string(i.ID())
			post.PkgID = string(i.ID())
			post.StatusCode = "Queued"
			req, err := http.PostForm(link, url.Values{"PkgID": {post.PkgID}, "StatusCode": {post.StatusCode}})
			_ = req
			_ = err
			return false
		}
	}
	var post Pkg
	link := "https://localhost:10000/pkg/" + string(i.ID())
	post.PkgID = string(i.ID())
	post.StatusCode = "Building"
	req, err := http.PostForm(link, url.Values{"PkgID": {post.PkgID}, "StatusCode": {post.StatusCode}})
	_ = req
	_ = err
	return true
}
func Build(g *pkggraph.PkgGraph, ch chan graph.Node) bool {
	var i graph.Node
	i = <-ch
	if CheckBuild(g, i) {
		fmt.Println(<-ch)
		var post Pkg
		link := "https://localhost:10000/pkg/" + string(i.ID())
		post.PkgID = string(i.ID())
		post.StatusCode = "Built"
		req, err := http.PostForm(link, url.Values{"PkgID": {post.PkgID}, "StatusCode": {post.StatusCode}})
		_ = req
		_ = err
		return true
	}
	return false
}
func main() {
	logger.InitBestEffort("/tmp/somelog", "INFO")
	file := "/home/rakshaa/CBL-Mariner/toolkit/tools/pkgparallel/threads/cdrkit.dot"
	g := pkggraph.NewPkgGraph()
	fmt.Printf("NewPKGGraph: %#v\n", g)
	err := pkggraph.ReadDOTGraphFile(g, file)
	if err != nil {
		log.Fatal(err)
	}

	leader := Clusterise.Clusterise(g)
	lists := make(map[graph.Node][]graph.Node)
	for key, element := range leader {
		lists[element] = append(lists[element], key)
	}
	var q [][]graph.Node
	for _, element := range lists {
		var l []graph.Node
		for _, i := range element {
			l = append(l, i)
		}
		q = append(q, l)
	}
	q0 := q[0]
	q1 := q[1]
	go func() {
		for len(q0) > 0 {
			var ch chan graph.Node
			ch <- q0[0]
			if Build(g, ch) {
				q0 = q0[1:]
			} else {
				pkg := q0[0]
				q0 = append(q0, pkg)
				q0 = q0[1:]
			}
		}
	}()
	go func() {
		for len(q1) > 0 {
			var ch chan graph.Node
			ch <- q1[0]
			if Build(g, ch) {
				q1 = q1[1:]
			} else {
				pkg := q1[0]
				q1 = append(q1, pkg)
				q1 = q1[1:]
			}
		}
	}()
}
