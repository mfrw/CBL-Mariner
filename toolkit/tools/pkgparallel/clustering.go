package clusterise

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

func CompTopLevels(g *pkggraph.PkgGraph) map[*pkggraph.PkgNode]int{
	top:= make(map[*pkggraph.PkgNode]int)
	V:= g.AllNodes()
	source:= make(*pkggraph.PkgNode)
	for _, u := range V{
		if (pkggraph.AllNodesFrom(u)==V){
			source = u
			break
		}
	}
	for _,u := range V{
		path, dist := graph.ShortestPath(g,source.ID(),u.ID())
		top[u]=dist
	}
	return top
}
func Contains(s []*pkggraph.PkgNode, e *pkggraph.PkgNode) bool {
    for _, a := range s {
        if a == e {
            return true
        }
    }
    return false
}

func DetectCycle(u *pkggraph.PkgNode, v *pkggraph.PkgNode, g pkggraph.PkgGraph, leader map[*pkggraph.PkgNode]*pkggraph.PkgNode, top map[*pkggraph.PkgNode]int){
	visited:= make(map[*pkggraph.PkgNode]bool)
	V:= g.AllNodes()
	for _,u := range V{
		visited[u]=false
	}
	var t int
	var cluster []*pkggraph.PkgNode
	for _,node := range V{
		if (leader[node]==leader[v]){
			cluster = append(node)
		}
	}
	t = len(V)
	for _,node := range cluster{
		t=Min(t, top[node])
	}
	var q []*pkggraph.PkgNode
	visited[u] = true
	q = append(q, u)
	for len(q) > 0 {
		var w *pkggraph.PkgNode
		w, q = q[0], q[1:]
		for _, node := range simple.DirectedGraph.From(w) {
			if Contains(cluster,node){
				return true;
			}
			if (abs(top[node]-t)<=1){
				if !visited[node] {
				q = append(q, node)
				visited[node] = true
				}
			}
		}
		for _, node := range simple.DirectedGraph.To(w) {
			if Contains(cluster,node){
				return true;
			}
			if (abs(top[node]-t)<=1){
				if visited[node] {
					return true;
				}
				q = append(q, node)
				visited[node] = true
			}
		}
	}
	return false;
}

func clusterise(g *pkggraph.PkgGraph) map[*pkggraph.PkgNode]*pkggraph.PkgNode {
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
		for _,v := range Union(simple.directedGraph.From(u.ID()), simple.directedGraph.To(u.ID())){
			if (absolute(top[u]-top[v])>1){
				continue
			}
			if (Contains(simple.directedGraph.From(u.ID()),v)){
				if (markup[v]){
					continue
				}
				if (DetectCycle(u, v, g, leader, top)){
					continue
				}
				leader[u]=leader[v]
				markup[u]=true
				markdown[v]=true
			}
			if (Contains(simple.directedGraph.To(u.ID()),v)){
				if (markdown[v]){
					continue
				}
				if (DetectCycle(u, v, g, leader, top)){
					continue
				}
				leader[u]=leader[v]
				markdown[u]=true
				markup[v]=true
			}
		}
	}
	return leader
}
