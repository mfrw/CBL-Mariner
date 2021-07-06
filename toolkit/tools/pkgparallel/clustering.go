package main

import (
	"fmt"

	"gonum.org/v1/gonum/graph"
	"gonum.org/v1/gonum/graph/encoding"
	"gonum.org/v1/gonum/graph/encoding/dot"
	"gonum.org/v1/gonum/graph/simple"
	"gonum.org/v1/gonum/graph/traverse"
	"microsoft.com/pkggen/internal/pkggraph"

	"pkggraph"
)

func CompTopLevels(g *pkggraph.PkgGraph) []*pkggraph.PkgNode{
	
}
func contains(s []*pkggraph.PkgNode, e *pkggraph.PkgNode) bool {
    for _, a := range s {
        if a == e {
            return true
        }
    }
    return false
}

func clusterise(g *pkggraph.PkgGraph, n pkggraph.PkgNode) []*pkggraph.PkgGraph {
	top:=CompTopLevels(g)
	V:= g.AllNodes()
	markup:= make(map[*pkggraph.PkgNode]bool)
	markdown:= make(map[*pkggraph.PkgNode]bool)
	leader:= make(map[*pkggraph.PkgNode]*pkggraph.PkgNode)
	for _, u := range V{
		markup[u] = false
		markdown[u] = false
		leader[u] = u
	}
	for _, u := range V{
		if (markup[u]&&markdown[u])
			continue
		for _,v := range Union(simple.directedGraph.From(u), simple.directedGraph.To(u)){
			if (absolute(top[u]-top[v])>1){
				continue
			}
			if (contains(simple.directedGraph.From(u),v)){
				if (markup[v])
					continue
				if (DetectCycle(u, v, g, leader))
					continue
				leader[u]=leader[v]
				markup[u]=markdown[v]=true
			}
			if (contains(simple.directedGraph.To(u),v)){
				if (markdown[v])
					continue
				if (DetectCycle(u, v, g, leader))
					continue
				leader[u]=leader[v]
				markdown[u]=markup[v]=true
			}
		}
	}
	return leader
}

func main() {

}