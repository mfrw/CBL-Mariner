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
	// "os/exec"
	// "crypto/tls"
	// "strings"
	"bytes"
	"strconv"
	// "time"
	"sync"
	"gonum.org/v1/gonum/graph"
	// "os"
	"microsoft.com/pkggen/internal/logger"
	"microsoft.com/pkggen/internal/pkggraph"
	"microsoft.com/pkggen/internal/rpm"

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
	// fmt.Println(dep)
	if len(dep) == 0 {
		client := &http.Client{}
		link := "http://localhost:10000/pkg/"+strconv.Itoa(int(i.ID()))
		resp, _ := http.Get(link)
		// fmt.Println(resp)
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
		// fmt.Println(req, err)
		// _ = resp
		_ = err
		req.Body.Close()
		resp.Body.Close()
		str :="Built "+responseObject.PkgID
		fmt.Println(str)
		return true
	}
	for _, node := range dep {
		id := node.ID()
		ID := strconv.Itoa(int(id))
		// str :=strings.Split(string(id),"x")
		// _=str
		// str = str[:1]
		link := "http://localhost:10000/pkg/"+ID
		resp, _ := http.Get(link)
		// fmt.Println(resp)
		bodyBytes, _ := ioutil.ReadAll(resp.Body)
		// fmt.Println(bodyBytes)
		// if err != nil {
		// 	fmt.Print(err.Error())
		// }
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
				// fmt.Println(req, err)
				// _ = resp
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
			
			// client = &http.Client{}
			req, err := http.NewRequest("PATCH", link, bytes.NewBuffer(j) )
			resp, err := client.Do(req)
			// fmt.Println(req, err)
			// _ = resp
			_ = err
			req.Body.Close()
			resp.Body.Close()
			str := post.StatusCode+" "+post.PkgID
			fmt.Println(str)
			// defer resp.Body.Close()
			// defer req.Body.Close()
			// fmt.Println(post.StatusCode)
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
				// fmt.Println(req, err)
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
			// client = &http.Client{}
			req, err := http.NewRequest("PATCH", link, bytes.NewBuffer(j) )
			resp, err := client.Do(req)
			// fmt.Println(req, err)
			_ = resp
			_ = err
			req.Body.Close()
			resp.Body.Close()
			str := post.StatusCode+" "+post.PkgID
			fmt.Println(str)
			// resp, err := client.Do(req)
			// defer resp.Body.Close()
			// defer req.Body.Close()
			// fmt.Println(post.StatusCode)
			return true
		}	
	}
	return true
}
func Build(g *pkggraph.PkgGraph, i graph.Node) bool {
	if CheckBuild(g, i) {
		// str:= i.ID()
		// tr := &http.Transport{
		// 	TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
		// }
		// client := &http.Client{Transport: tr}
		var post Pkg
		str := strconv.Itoa(int(i.ID()))
		link := "http://localhost:10000/pkg/"+str
		resp, _ := http.Get(link)
		// fmt.Println(resp)
		bodyBytes, _ := ioutil.ReadAll(resp.Body)
		// fmt.Println(bodyBytes)
		// if err != nil {
		// 	fmt.Print(err.Error())
		// }
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
		
		// os.Chdir("/home/rakshaa/CBL-Mariner/toolkit")
		// command:= "REBUILD_TOOLS=y"
		// cmd := exec.Command("sudo", "make", "toolchain", command)
		// out, err := cmd.Output()

		// cmd.Stderr = os.Stderr
		// cmd.Stdin = os.Stdin
		// out, err := cmd.Output()
		// command:= "SPECS_DIR="+path
		// cmd := exec.Command("sudo", "make", "build-packages", command)
		// cmd.Stderr = os.Stderr
		// cmd.Stdin = os.Stdin

		// out, err := cmd.Output()
		// if err != nil {
		// 	fmt.Println("Err", err)
		// } else {
		// 	fmt.Println("OUT:", string(out))
		// }
		defines:= rpm.DefaultDefines()
		defines[rpm.DistTagDefine] = ".cm1"
		defines[rpm.DistroReleaseVersionDefine] = "1.0.20210721.1210"
		defines[rpm.DistroBuildNumberDefine] = "75b97587"
		err1:=rpm.BuildRPMFromSRPM(post.Location, defines, "")
		// var js = []byte(j)
		// jstr := string(js)
		fmt.Println(err1)
		req, err := http.NewRequest("PATCH", link, bytes.NewBuffer(j) )
		resp, err = client.Do(req)
		// fmt.Println(req, err)
		// _ = resp
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
	file := "/home/rakshaa/CBL-Mariner/toolkit/tools/pkgparallel/files/reverse-cdrkit.dot"
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
			// jstr := string(js)
			client := &http.Client{}
			req, err:= http.NewRequest("POST", link, bytes.NewBuffer(j))
			// fmt.Println(req)
			_, _ = client.Do(req)
			_=err
			req.Body.Close()
			str = post.StatusCode+" "+post.PkgID
			fmt.Println(str)
			// defer resp.Body.Close()
			// defer req.Body.Close()
		}
		q = append(q, l)
	}
	//As of now only two currently
	//To be in loop
	var wg sync.WaitGroup
	wg.Add(len(q))
	for i:=0; i<len(q); i++ {
		fmt.Println("Cluster for")
		go func() {
			for len(q[i]) > 0 && i< len(q){
				//Find the best VM pool to work with and then push the job there
				fmt.Println("Package for")
				fmt.Println("Package: ", q[i])
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