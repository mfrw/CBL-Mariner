package clusterise

import (
	"math"
	"fmt"
	"gonum.org/v1/gonum/graph"
	"gonum.org/v1/gonum/graph/path"
	"microsoft.com/pkggen/internal/pkggraph"
)

func ShortestPath(g *pkggraph.PkgGraph,u graph.Node,v graph.Node) int64 {
	lol:= graph.Graph(g)
	paths:= path.DijkstraFrom(u, lol)
	return int64(paths.WeightTo(v.ID()))
}
func Union(a, b []graph.Node) []graph.Node{
	m := make(map[graph.Node]bool)

	for _, item := range a {
			m[item] = true
	}

	for _, item := range b {
			if _, ok := m[item]; !ok {
					a = append(a, item)
			}
	}
	return a
}

func CompTopLevels(g *pkggraph.PkgGraph) map[graph.Node]int64{
	top:= make(map[graph.Node]int64)
	V:= g.AllNodes()
	var source graph.Node
	for i, u := range V{
		D:=V
		D=append(D[:i], D[i+1:]...)
		if (graph.NodesOf(g.To(u.ID()))==nil){
			source = u
			break
		}
	}
	for _,u := range V{
		dist := ShortestPath(g,source,u)
		fmt.Println(u, dist)
		if dist == int64(math.Inf(1)){
			dist = 0
		}
		top[u]=dist
	}
	return top
}
func Contains(s []graph.Node, e graph.Node) bool {
    for _, a := range s {
        if a == e {
            return true
        }
    }
    return false
}

func DetectCycle(u graph.Node, v graph.Node, g *pkggraph.PkgGraph, leader map[graph.Node]graph.Node, top map[graph.Node]int64) bool{
	visited:= make(map[graph.Node]bool)
	V:= g.AllNodes()
	for _,u := range V{
		visited[u]=false
	}
	var t int64
	var cluster []graph.Node
	for _,node := range V{
		if (leader[node]==leader[v]){
			cluster = append(cluster, node)
		}
	}
	t = int64(len(V))
	for _,node := range cluster{
		t= int64(math.Min(float64(t), float64(top[node])))
	}
	var q []graph.Node
	visited[u] = true
	q = append(q, u)
	for len(q) > 0 {
		var w graph.Node
		w, q = q[0], q[1:]
		for _, node := range Union(graph.NodesOf(g.From(w.ID())),graph.NodesOf(g.To(w.ID()))){
			if Contains(cluster,node){
				return true;
			}
			if (int64(math.Abs(float64(top[node]-t)))<=1){
				if !visited[node] {
				q = append(q, node)
				visited[node] = true
				} else {
					return true
				}
			}
		}
	}
	return false;
}

func Clusterise(g *pkggraph.PkgGraph) map[graph.Node]graph.Node {
	fmt.Println("Inside Clusterise")
	top:=CompTopLevels(g)
	V:= g.AllNodes()
	markup:= make(map[graph.Node]bool)
	markdown:= make(map[graph.Node]bool)
	leader:= make(map[graph.Node]graph.Node)
	for _, u := range V{
		markup[u] = false
		markdown[u] = false
		leader[u] = u
	}
	for _, u := range V{
		if (markup[u]&&markdown[u]){
			continue
		}
		for _,v := range Union(graph.NodesOf(g.From(u.ID())), graph.NodesOf(g.To(u.ID()))){
			if (int64(math.Abs(float64(top[u]-top[v])))>1){
				continue
			}
			if (Contains(graph.NodesOf(g.From(u.ID())),v)){
				if (markup[v]){
					continue
				}
				leader[u]=leader[v]
				markup[u]=true
				markdown[v]=true
			}
			if (Contains(graph.NodesOf(g.To(u.ID())),v)){
				if (markdown[v]){
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
