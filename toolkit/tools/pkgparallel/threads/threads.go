// Go program to illustrate send
// and receive operation
package main

import (
	"fmt"
	"microsoft.com/pkggen/internal/pkggraph"
	"microsoft.com/pkggen/pkgparallel/clustering"
)

func myfunc(ch chan graph.Node) {
	fmt.Println(234 + <-ch)
}
func main() {
	ch := make(chan graph.Node)
	file := "./cdrkit.dot"
	g := pkggraph.NewPkgGraph()
	err := pkggraph.ReadDOTGraphFile(g, file)
	leader := Clusterise.Clusterise(g)
	lists:= make(map[graph.Node][]graph.Node)
	for key, element in range leader{
		lists[element] = append(lists[element],key)
	}
	for key, element := range lists{
		for i in range element{
			ch<-i
		}
	}
}
