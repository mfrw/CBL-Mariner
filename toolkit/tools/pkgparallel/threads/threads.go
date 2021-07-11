// Go program to illustrate send
// and receive operation
package main

import (
	"fmt"
	"microsoft.com/pkggen/internal/pkggraph"
)

func myfunc(ch chan int) {
	fmt.Println(234 + <-ch)
}
func main() {
	fmt.Println("start Main method")
	// Creating a channel
	ch := make(chan int)

	go myfunc(ch)
	ch <- 23
	fmt.Println("End Main method")
}
