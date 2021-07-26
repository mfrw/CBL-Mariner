// Go program to illustrate send
// and receive operation
package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os/exec"
	"bytes"
	"strconv"
	"sync"
	"gonum.org/v1/gonum/graph"
	"microsoft.com/pkggen/internal/logger"
	"microsoft.com/pkggen/internal/pkggraph"
	clusterise "microsoft.com/pkggen/pkgparallel/clustering"
)

type Pkg struct {
	PkgID      string `json:"PkgID" bson:"PkgID"`
	StatusCode string `json:"StatusCode" bson:"StatusCode"`
	Location string `json:"Location" bson:"Location"`
}

func CheckBuild(g *pkggraph.PkgGraph, i graph.Node) bool {
	dep := graph.NodesOf(g.From(i.ID()))
	if len(dep) == 0 {
		client := &http.Client{}
		link := "http://localhost:10000/pkg/"+strconv.Itoa(int(i.ID()))
		resp, _ := http.Get(link)
		bodyBytes, _ := ioutil.ReadAll(resp.Body)
		resp.Body.Close()
		var responseObject Pkg
		json.Unmarshal(bodyBytes, &responseObject)
		j,_:=json.Marshal(map[string]interface{}{
			"PkgID": responseObject.PkgID,
			"StatusCode":"Built",
			"Location":responseObject.Location,
		}) 
		req, err := http.NewRequest("PATCH", link, bytes.NewBuffer(j) )
		resp, err = client.Do(req)
		_ = err
		req.Body.Close()
		resp.Body.Close()
		str :="Built "+responseObject.PkgID
		fmt.Println(str)
		return true
	}
	for _, node := range dep {
		for _,i := range g.AllNodes(){
			if node.ID() == i.ID(){
				if i.Type.String()!="Build" || i.State.String()=="Meta"{
					break
				} else {
					id := node.ID()
		ID := strconv.Itoa(int(id))
		link := "http://localhost:10000/pkg/"+ID
		resp, _ := http.Get(link)
		bodyBytes, _ := ioutil.ReadAll(resp.Body)
		resp.Body.Close()
		var responseObject Pkg
		json.Unmarshal(bodyBytes, &responseObject)
		if responseObject.StatusCode != "Built" {
			var post Pkg
			link := "http://localhost:10000/pkg/" +strconv.Itoa(int(i.ID()))
			post.StatusCode = "Queued"
			client := &http.Client{}
			if responseObject.Location=="" || responseObject.Location=="<NO-SRPM-PATH>"{
				j,_:=json.Marshal(map[string]interface{}{
					"PkgID": responseObject.PkgID,
					"StatusCode":"Built",
					"Location":responseObject.Location,
				}) 
				req, err := http.NewRequest("PATCH", link, bytes.NewBuffer(j) )
				resp, err := client.Do(req)
				_ = err
				req.Body.Close()
				resp.Body.Close()
				str := post.StatusCode+" "+post.PkgID
				fmt.Println(str)
				return true
			}
			j,_:=json.Marshal(map[string]interface{}{
				"PkgID": responseObject.PkgID,
				"StatusCode":post.StatusCode,
				"Location":responseObject.Location,
			}) 
			
			req, err := http.NewRequest("PATCH", link, bytes.NewBuffer(j) )
			resp, err := client.Do(req)
			_ = err
			req.Body.Close()
			resp.Body.Close()
			str := post.StatusCode+" "+post.PkgID
			fmt.Println(str)
			return false
			} else {
			var post Pkg
			link := "http://localhost:10000/pkg/"+ strconv.Itoa(int(i.ID()))
			post.StatusCode = "Building"
			client := &http.Client{}
			if responseObject.Location =="" || responseObject.Location=="<NO-SRPM-PATH>"{
				j,_:=json.Marshal(map[string]interface{}{
					"PkgID": responseObject.PkgID,
					"StatusCode":"Built",
					"Location":responseObject.Location,
				}) 
				req, err := http.NewRequest("PATCH", link, bytes.NewBuffer(j) )
				resp, err := client.Do(req)
				_ = resp
				_ = err
				req.Body.Close()
				resp.Body.Close()
				str := post.StatusCode+" "+post.PkgID
				fmt.Println(str)
				return true
			}
			j,_:=json.Marshal(map[string]interface{}{
				"PkgID": responseObject.PkgID,
				"StatusCode":post.StatusCode,
				"Location":responseObject.Location,
			}) 
			req, err := http.NewRequest("PATCH", link, bytes.NewBuffer(j) )
			resp, err := client.Do(req)
			_ = resp
			_ = err
			req.Body.Close()
			resp.Body.Close()
			str := post.StatusCode+" "+post.PkgID
			fmt.Println(str)
			return true
		}	
				}
			}
		}
		
	}
	return true
}
func Build(g *pkggraph.PkgGraph, i graph.Node) bool {
	if CheckBuild(g, i) {
		var post Pkg
		str := strconv.Itoa(int(i.ID()))
		link := "http://localhost:10000/pkg/"+str
		resp, _ := http.Get(link)
		bodyBytes, _ := ioutil.ReadAll(resp.Body)
		resp.Body.Close()
		var responseObject Pkg
		json.Unmarshal(bodyBytes, &responseObject)
		post.PkgID = str
		post.StatusCode = "Built"
		post.Location = responseObject.Location
		client:=&http.Client{}
		if post.Location=="" || post.Location=="<NO-SRPM-PATH>"{
			j,_:=json.Marshal(map[string]interface{}{
				"PkgID": post.PkgID,
				"StatusCode":"Built",
				"Location":post.Location,
			}) 
			req, err := http.NewRequest("PATCH", link, bytes.NewBuffer(j) )
			resp, err := client.Do(req)
			_ = resp
			_ = err
			req.Body.Close()
			resp.Body.Close()
			return true
		}
		j,_:=json.Marshal(map[string]interface{}{
			"PkgID": post.PkgID,
			"StatusCode":post.StatusCode,
			"Location":post.Location,
		}) 
		cmd := exec.Command("sudo", "rpmbuild", "-rc", post.Location, "--rebuild", "--nodeps")
		out, err := cmd.Output()
		if err != nil {
			fmt.Println("Error: ", err)
		}
		fmt.Println(string(out))
		req, err := http.NewRequest("PATCH", link, bytes.NewBuffer(j) )
		resp, err = client.Do(req)
		_ = err
		req.Body.Close()
		resp.Body.Close()
		fmt.Println("After Build func.")
		str = post.StatusCode+" "+post.PkgID
		fmt.Println(str)
		return true
	}
	return false
}
func main() {
	logger.InitBestEffort("/tmp/somelog", "INFO")
	file := "/home/rakshaa/CBL-Mariner/toolkit/tools/depsearch/flex.dot"
	// file:="/home/rakshaa/CBL-Mariner/toolkit/tools/pkgparallel/files/reverse-cdrkit.dot"
	g := pkggraph.NewPkgGraph()
	err := pkggraph.ReadDOTGraphFile(g, file)
	if err != nil {
		log.Fatal(err)
	}

	leader := clusterise.Clusterise(g)
	lists := make(map[graph.Node][]graph.Node)
	for key, _:= range leader{
		for _,i := range g.AllNodes(){
			if key.ID() == i.ID(){
				if i.Type.String()!="Build" || i.State.String()=="Meta" || i.State.String()=="Unresolved"{
					delete(leader, key);
					break
				} 
				
			} else {
				continue
			}
		}
	}
	for key, element := range leader {
		for _,i := range g.AllNodes(){
			if element.ID() == i.ID(){
				if i.Type.String()!="Build" || i.State.String()=="Meta" || i.State.String()=="Unresolved"{
					break
				} 
					lists[element] = append(lists[element], key)
				
			} else {
				continue
			}
		}
	}
	var q [][]graph.Node
	for _, element := range lists {
		var l []graph.Node
		for _, i := range element {
			l = append(l, i)
			var post Pkg
			str := strconv.Itoa(int(i.ID()))
			link := "http://localhost:10000/pkg"
			post.PkgID = str
			post.StatusCode = "Starting"
			path:=""
			for _, element := range g.AllNodes(){
				if element.ID() == i.ID(){
					path = element.SrpmPath
					break
				}
			}
			post.Location = path
			if path == "" || path =="<NO_SRPM_PATH>"{
				post.StatusCode="Built"
			}
			j,_:=json.Marshal(map[string]interface{}{
				"PkgID": post.PkgID,
				"StatusCode":post.StatusCode,
				"Location":post.Location,
			}) 
		
			client := &http.Client{}
			req, err:= http.NewRequest("POST", link, bytes.NewBuffer(j))
			
			_, _ = client.Do(req)
			_=err
			req.Body.Close()
			str = post.StatusCode+" "+post.PkgID
			fmt.Println(str)
		}
		q = append(q, l)
	}
	
	var wg sync.WaitGroup
	for i:=0; i<len(q); i++{
		wg.Add(1)
		fmt.Println("Cluster for")
		go func() {
			for len(q[i]) > 0{
				//Find the best VM pool to work with and then push the job there
				fmt.Println("Package for")
				fmt.Println("Package: ", q[i][0])
				if Build(g, q[i][0]) {
					if len(q[i])==1{
						break
					} else {
						q[i] = q[i][1:]
					}
				} else {
						pkg := q[i][0]
						q[i] = append(q[i], pkg)
						q[i] = q[i][1:]
					}
				}
			
			wg.Done()
		}()
		wg.Wait()
	}

}