package main

import (
	"fmt"
	"os/exec"
)

func main(){
	out, err := exec.Command("sudo go run depsearch.go --input=home/rakshaa/CBL-Mariner/build/pkg_artifacts/graph.dot --output=cdrkit.dot --packages='cdrkit'").Output()

    // if there is an error with our execution
    // handle it here
    if err != nil {
        fmt.Printf("%s", err)
    }
    // as the out variable defined above is of type []byte we need to convert
    // this to a string or else we will see garbage printed out in our console
    // // this is how we convert it to a string
    // fmt.Println("Command Successfully Executed")
    output := string(out[:])
    fmt.Println(output)
}
