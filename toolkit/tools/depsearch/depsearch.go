// Copyright (c) Microsoft Corporation.
// Licensed under the MIT License.

package main

import (
	"fmt"
	"os"

	"gonum.org/v1/gonum/graph"
	"gopkg.in/alecthomas/kingpin.v2"

	"microsoft.com/pkggen/internal/exe"
	"microsoft.com/pkggen/internal/logger"
	"microsoft.com/pkggen/internal/pkggraph"
)

var (
	app = kingpin.New("depsearch", "Returns a list of everything that depends on a given package or spec")

	inputGraphFile  = exe.InputFlag(app, "Path to the DOT graph file to search.")
	outputGraphFile = exe.OutputFlag(app, "Path to save the graph.")

	pkgsToSearch  = app.Flag("packages", "Space seperated list of packages to search from.").String()
	specsToSearch = app.Flag("specs", "Space seperated list of specfiles to search from.").String()
	goalsToSearch = app.Flag("goals", "Space seperated list of goal names to search (Try 'ALL' or 'PackagesToBuild').").String()

	reverseSearch = app.Flag("reverse", "Reverse the search to give a traditional dependency list for the packages instead of dependants.").Bool()

	logFile  = exe.LogFileFlag(app)
	logLevel = exe.LogLevelFlag(app)
)

func main() {
	var (
		outputGraph *pkggraph.PkgGraph
	)

	app.Version(exe.ToolkitVersion)
	kingpin.MustParse(app.Parse(os.Args[1:]))
	logger.InitBestEffort(*logFile, *logLevel)

	graph := pkggraph.NewPkgGraph()
	err := pkggraph.ReadDOTGraphFile(graph, *inputGraphFile)
	if err != nil {
		logger.Log.Panicf("Failed to read DOT graph with error: %s", err)
	}

	pkgSearchList := exe.ParseListArgument(*pkgsToSearch)
	specSearchList := exe.ParseListArgument(*specsToSearch)
	goalSearchList := exe.ParseListArgument(*goalsToSearch)

	nodeListPkg := searchForPkg(graph, pkgSearchList)
	nodeListSpec := searchForSpec(graph, specSearchList)
	nodeListGoal := searchForGoal(graph, goalSearchList)

	nodeLists := append(nodeListPkg, append(nodeListSpec, nodeListGoal...)...)
	nodeSet := removeDuplicates(nodeLists)

	if len(nodeSet) == 0 {
		logger.Log.Panicf("Could not find any nodes matching pkgs:[%s] or specs:[%s] or goals[%s]", *pkgsToSearch, *specsToSearch, *goalsToSearch)
	} else {
		logger.Log.Infof("Found %d nodes to consider", len(nodeSet))
	}

	if *reverseSearch {
		logger.Log.Infof("Forward dependency search")
		outputGraph, err = buildRequiresGraph(graph, nodeSet)
	} else {
		logger.Log.Infof("Backwards dependants search")
		outputGraph, err = buildDependsOnGraph(graph, nodeSet)
	}

	printSpecs(outputGraph)

	pkggraph.WriteDOTGraphFile(outputGraph, *outputGraphFile)
}

func searchForGoal(graph *pkggraph.PkgGraph, goals []string) (list []*pkggraph.PkgNode) {
	for _, goal := range goals {
		n := graph.FindGoalNode(goal)
		if n != nil {
			list = append(list, n)
		}
	}
	return
}

func searchForPkg(graph *pkggraph.PkgGraph, packages []string) (list []*pkggraph.PkgNode) {
	for _, n := range graph.AllRunNodes() {
		nodeName := n.VersionedPkg.Name
		for _, searchName := range packages {
			if nodeName == searchName {
				list = append(list, n)
			}
		}
	}
	return
}

func searchForSpec(graph *pkggraph.PkgGraph, specs []string) (list []*pkggraph.PkgNode) {
	for _, n := range graph.AllRunNodes() {
		nodeSpec := n.SpecName()
		for _, searchSpec := range specs {
			if nodeSpec == searchSpec {
				list = append(list, n)
			}
		}
	}
	return
}

func removeDuplicates(nodeList []*pkggraph.PkgNode) (uniqueNodeList []*pkggraph.PkgNode) {
	nodeMap := make(map[*pkggraph.PkgNode]bool)
	for _, n := range nodeList {
		nodeMap[n] = true
	}
	uniqueNodeList = make([]*pkggraph.PkgNode, 0, len(nodeMap))
	for key, _ := range nodeMap {
		uniqueNodeList = append(uniqueNodeList, key)
	}
	return
}

func buildRequiresGraph(graphIn *pkggraph.PkgGraph, nodeList []*pkggraph.PkgNode) (graphOut *pkggraph.PkgGraph, err error) {
	newGraph := pkggraph.NewPkgGraph()

	// Make a copy of the graph
	newGraph, err = graphIn.DeepCopy()
	if err != nil {
		return
	}

	// Add a goal node to all the things we care about
	root := newGraph.AddMetaNode(nil, nodeList)
	graphOut, err = newGraph.CreateSubGraph(root)
	if err != nil {
		return
	}

	return
}

func buildDependsOnGraph(graphIn *pkggraph.PkgGraph, nodeList []*pkggraph.PkgNode) (graphOut *pkggraph.PkgGraph, err error) {
	reversedGraph := pkggraph.NewPkgGraph()

	// Make a copy of the graph
	reversedGraph, err = graphIn.DeepCopy()
	if err != nil {
		return
	}

	// Then reverse every edge in the graph
	for _, edge := range graph.EdgesOf(reversedGraph.Edges()) {
		reversedGraph.RemoveEdge(edge.From().ID(), edge.To().ID())
		reversedGraph.SetEdge(edge.ReversedEdge())
	}

	// Add a goal node to all the things we care about
	root := reversedGraph.AddMetaNode(nil, nodeList)
	graphOut, err = reversedGraph.CreateSubGraph(root)
	if err != nil {
		return
	}

	return
}

func printSpecs(graph *pkggraph.PkgGraph) {
	specs := make(map[string]bool)
	for _, n := range graph.AllNodes() {
		if n.Type == pkggraph.TypeRun {
			nodeSpec := n.SpecName()
			specs[nodeSpec] = true
		}
	}

	for key, _ := range specs {
		fmt.Printf("\t%s\n", key)
	}
}
