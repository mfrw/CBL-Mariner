// Go program to illustrate send
// and receive operation
package main

import (
	"fmt"
	"gonum.org/v1/gonum/graph"
	"gonum.org/v1/gonum/graph/path"
	"microsoft.com/pkggen/internal/pkggraph"
	"microsoft.com/pkggen/pkgparallel/unravel"
)

func myfunc(ch chan int) {
	fmt.Println(234 + <-ch)
}
func main() {
	ch := make(chan map[graph.Node]graph.Node)

	go myfunc(ch)
	ch <- 23
	fmt.Println("End Main method")
}
