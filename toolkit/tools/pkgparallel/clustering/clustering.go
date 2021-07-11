package clusterise

import (
	"math"
	"reflect"

	"microsoft.com/pkggen/internal/pkggraph"
)

func ShortestPath(g *pkggraph.PkgGraph,u *pkggraph.PkgNode,v *pkggraph.PkgNode) int64 {
	if (!g.HasEdgeFromTo(u.ID(),v.ID())){
		return 0
	}
	return 1
}

func CompTopLevels(g *pkggraph.PkgGraph) map[*pkggraph.PkgNode]int64{
	top:= make(map[*pkggraph.PkgNode]int64)
	V:= g.AllNodes()
	var source *pkggraph.PkgNode
	for _, u := range V{
		if (reflect.DeepEqual(g.AllNodesFrom(u),V)){
			source = u
			break
		}
	}
	for _,u := range V{
		dist := ShortestPath(g,source,u)
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

func DetectCycle(u *pkggraph.PkgNode, v *pkggraph.PkgNode, g pkggraph.PkgGraph, leader map[*pkggraph.PkgNode]*pkggraph.PkgNode, top map[*pkggraph.PkgNode]int64) bool{
	visited:= make(map[*pkggraph.PkgNode]bool)
	V:= g.AllNodes()
	for _,u := range V{
		visited[u]=false
	}
	var t int64
	var cluster []*pkggraph.PkgNode
	for _,node := range V{
		if (leader[node]==leader[v]){
			cluster = append(cluster, node)
		}
	}
	t = len(V)
	for _,node := range cluster{
		t=math.Min(t, top[node])
	}
	var q []*pkggraph.PkgNode
	visited[u] = true
	q = append(q, u)
	for len(q) > 0 {
		var w *pkggraph.PkgNode
		w, q = q[0], q[1:]
		for _, node := range g.From(w.ID()) {
			if Contains(cluster,node){
				return true;
			}
			if (math.Abs(top[node]-t)<=1){
				if !visited[node] {
				q = append(q, node)
				visited[node] = true
				}
			}
		}
		for _, node := range g.To(w.ID()) {
			if Contains(cluster,node){
				return true;
			}
			if (math.Abs(top[node]-t)<=1){
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
		if (markup[u]&&markdown[u]){
			continue
		}
		for _,v := range Union(g.From(u.ID()), g.To(u.ID())){
			if (math.Abs(top[u]-top[v])>1){
				continue
			}
			if (Contains(g.From(u.ID()),v)){
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
			if (Contains(g.To(u.ID()),v)){
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
