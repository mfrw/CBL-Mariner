// Go program to illustrate send
// and receive operation
package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	// "net/url"
	"os/exec"
	// "crypto/tls"
	// "strings"
	"bytes"
	"strconv"
	// "time"
	"sync"
	"gonum.org/v1/gonum/graph"
	"microsoft.com/pkggen/internal/logger"
	"microsoft.com/pkggen/internal/pkggraph"

	// "microsoft.com/pkggen/pkgparallel/apirequests"
	clusterise "microsoft.com/pkggen/pkgparallel/clustering"
)

type Pkg struct {
	PkgID      string `json:"PkgID" bson:"PkgID"`
	StatusCode string `json:"StatusCode" bson:"StatusCode"`
	Location string `json:"Location" bson:"Location"`
}

func CheckBuild(g *pkggraph.PkgGraph, i graph.Node) bool {
	dep := graph.NodesOf(g.From(i.ID()))
	for _, node := range dep {
		id := node.ID()
		ID := strconv.Itoa(int(id))
		// str :=strings.Split(string(id),"x")
		// _=str
		// str = str[:1]
		link := "http://localhost:10000/pkg/"+ID
		resp, err := http.Get(link)
		resp.Body.Close()
		if err != nil {
			fmt.Print(err)
		}
			if resp==nil {
			// defer resp.Body.Close()
			var post Pkg
			link := "http://localhost:10000/pkg" + strconv.Itoa(int(i.ID()))
			post.PkgID = strconv.Itoa(int(i.ID()))
			post.StatusCode = "Queued"
			path:=""
			for _, element := range g.AllNodes(){
				// fmt.Println(element.ID())
				if element.ID() == i.ID(){
					path = element.SourceDir
					break
				}
			}
			// fmt.Println(path)
			post.Location = path
			client := &http.Client{}
			if path=="" || path=="<NO-SRPM-PATH>"{
				j,_:=json.Marshal(map[string]interface{}{
					"PkgID": post.PkgID,
					"StatusCode":"Built",
					"Location":post.Location,
				}) 
				req, err := http.NewRequest("PATCH", link, bytes.NewBuffer(j) )
				resp, err := client.Do(req)
				// fmt.Println(req, err)
				_ = resp
				_ = err
				req.Body.Close()
				resp.Body.Close()
				return true
			}
			j,_:=json.Marshal(map[string]string{
				"PkgID": post.PkgID,
				"StatusCode":post.StatusCode,
				"Location":post.Location,
			}) 
			// client = &http.Client{}
			req, err := http.NewRequest("PATCH", link, bytes.NewBuffer(j) )
			resp, err := client.Do(req)
			req.Body.Close()
			resp.Body.Close()
			// fmt.Println(req, err)
			_ = resp
			_ = err
			// defer resp.Body.Close()
			// resp, err := client.Do(req)
			// fmt.Println(post.StatusCode)
			return false
		} else {
			// defer resp.Body.Close()
			bodyBytes, _ := ioutil.ReadAll(resp.Body)
			// if err != nil {
			// 	fmt.Print(err.Error())
			// }
			var responseObject Pkg
			json.Unmarshal(bodyBytes, &responseObject)
			if responseObject.StatusCode != "Built" {
				var post Pkg
				link := "http://localhost:10000/pkg/" +strconv.Itoa(int(i.ID()))
				post.PkgID = strconv.Itoa(int(i.ID()))
				post.StatusCode = "Queued"
				path:=""
				for _, element := range g.AllNodes(){
					// fmt.Println(element.ID())
					if element.ID() == i.ID(){
						path = element.SourceDir
						break
					}
				}
				post.Location = path
				client := &http.Client{}
				if path=="" || path=="<NO-SRPM-PATH>"{
					j,_:=json.Marshal(map[string]interface{}{
						"PkgID": post.PkgID,
						"StatusCode":"Built",
						"Location":post.Location,
					}) 
					req, err := http.NewRequest("PATCH", link, bytes.NewBuffer(j) )
					resp, err := client.Do(req)
					// fmt.Println(req, err)
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
				
				// client = &http.Client{}
				req, err := http.NewRequest("PATCH", link, bytes.NewBuffer(j) )
				resp, err := client.Do(req)
				// fmt.Println(req, err)
				_ = resp
				_ = err
				req.Body.Close()
				resp.Body.Close()
				// defer resp.Body.Close()
				// defer req.Body.Close()
				// fmt.Println(post.StatusCode)
				return false
			}
		}
	}
	var post Pkg
	link := "http://localhost:10000/pkg/"+ strconv.Itoa(int(i.ID()))
	post.PkgID = strconv.Itoa(int(i.ID()))
	post.StatusCode = "Building"
	path:=""
	for _, element := range g.AllNodes(){
		// fmt.Println(element.ID())
		if element.ID() == i.ID(){
			path = element.SourceDir
			break
		}
	}
	post.Location = path
	client := &http.Client{}
	if path=="" || path=="<NO-SRPM-PATH>"{
		j,_:=json.Marshal(map[string]interface{}{
			"PkgID": post.PkgID,
			"StatusCode":"Built",
			"Location":post.Location,
		}) 
		req, err := http.NewRequest("PATCH", link, bytes.NewBuffer(j) )
		resp, err := client.Do(req)
		// fmt.Println(req, err)
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
	// client = &http.Client{}
	req, err := http.NewRequest("PATCH", link, bytes.NewBuffer(j) )
	resp, err := client.Do(req)
	// fmt.Println(req, err)
	_ = resp
	_ = err
	req.Body.Close()
	resp.Body.Close()
	// resp, err := client.Do(req)
	// defer resp.Body.Close()
	// defer req.Body.Close()
	// fmt.Println(post.StatusCode)
	return true
}
func Build(g *pkggraph.PkgGraph, i graph.Node) bool {
	if CheckBuild(g, i) {
		// str:= i.ID()
		var path string
		for _, element := range g.AllNodes(){
			// fmt.Println(element.ID())
			if element.ID() == i.ID(){
				path = element.SourceDir
				break
			}
		}
		// tr := &http.Transport{
		// 	TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
		// }
		// client := &http.Client{Transport: tr}
		var post Pkg
		str := strconv.Itoa(int(i.ID()))
		link := "http://localhost:10000/pkg/"+str
		post.PkgID = str
		post.StatusCode = "Built"
		post.Location = path
		client:=&http.Client{}
		if path=="" || path=="<NO-SRPM-PATH>"{
			j,_:=json.Marshal(map[string]interface{}{
				"PkgID": post.PkgID,
				"StatusCode":"Built",
				"Location":post.Location,
			}) 
			req, err := http.NewRequest("PATCH", link, bytes.NewBuffer(j) )
			resp, err := client.Do(req)
			// fmt.Println(req, err)
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
		// fmt.Println(post.StatusCode)
		
		command:= "sudo make build-packages SPEC_DIR="+path+" -j($nproc)"
		cmd := exec.Command("bash", "-c", command)
		err1 := cmd.Run()
		if err1 != nil {
			log.Println(err1)
			return false
		}
		
		// var js = []byte(j)
		// jstr := string(js)
		req, err := http.NewRequest("PATCH", link, bytes.NewBuffer(j) )
		resp, err := client.Do(req)
		// fmt.Println(req, err)
		_ = resp
		_ = err
		req.Body.Close()
		resp.Body.Close()
		return true
	}
	return false
}
func main() {
	logger.InitBestEffort("/tmp/somelog", "INFO")
	file := "/home/rakshaa/CBL-Mariner/toolkit/tools/pkgparallel/threads/cdrkit.dot"
	g := pkggraph.NewPkgGraph()
	// fmt.Printf("NewPKGGraph: %#v\n", g)
	err := pkggraph.ReadDOTGraphFile(g, file)
	if err != nil {
		log.Fatal(err)
	}

	leader := clusterise.Clusterise(g)
	lists := make(map[graph.Node][]graph.Node)
	for key, element := range leader {
		lists[element] = append(lists[element], key)
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
				// fmt.Println(element.ID())
				if element.ID() == i.ID(){
					path = element.SourceDir
					break
				}
			}
			post.Location = path
			j,_:=json.Marshal(map[string]interface{}{
				"PkgID": post.PkgID,
				"StatusCode":post.StatusCode,
				"Location":post.Location,
			}) 
			// jstr := string(js)
			client := &http.Client{}
			req, err:= http.NewRequest("POST", link, bytes.NewBuffer(j))
			// fmt.Println(req)
			resp, _ := client.Do(req)
			_=err
			req.Body.Close()
			resp.Body.Close()
			// defer req.Body.Close()
		}
		q = append(q, l)
	}
	//As of now only two currently
	//To be in loop
	var wg sync.WaitGroup
	wg.Add(len(q))
	for i:=0; i<len(q); i++ {
		go func() {
			for len(q[i]) > 0 && i< len(q){
				//Find the best VM pool to work with and then push the job there
				if Build(g, q[i][0]) {
					if len(q[i])==1{
						break
					} else {
						q[i] = q[i][1:]
					}
				} else {
					// if len(q[i])==1{
					// 	continue
					// } else {
						pkg := q[i][0]
						q[i] = append(q[i], pkg)
						q[i] = q[i][1:]
					}
				}
			
			wg.Done()
		}()
	// }
	wg.Wait()
}
}