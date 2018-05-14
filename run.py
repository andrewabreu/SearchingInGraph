# Search methods
# -*- coding: utf-8 -*-
import search

ab = search.GPSProblem('A', 'B', search.romania)
cn = search.GPSProblem('C', 'N', search.romania)
nt = search.GPSProblem('N', 'T', search.romania)
eo = search.GPSProblem('E', 'O', search.romania)
zv = search.GPSProblem('Z', 'V', search.romania)

#print("Breadth First Search")
#print search.breadth_first_graph_search(ab).path()

#print("Depth First Search")
#print search.depth_first_graph_search(ab).path()
# print search.iterative_deepening_search(ab).path()
# print search.depth_limited_search(ab).path()

print("Mapa de Carreteras de la Ciudad de Rumanía")
print("De la ciudad A a la ciudad B")
print("Branch and Bound Search")
print search.branch_and_bound_graph_search(ab).path()
print "Se expanden: " + str(search.get_nexpandnodes())

print('\n')

print("Branch and Bound with Underestimation Search")
print search.branch_and_bound_with_underestimation_graph_search(ab, ab.h).path()
print "Se expanden: " + str(search.get_nexpandnodes())

print('\n')

print("De la ciudad C a la ciudad N")
print("Branch and Bound Search")
print search.branch_and_bound_graph_search(cn).path()
print "Se expanden: " + str(search.get_nexpandnodes())

print('\n')

print("Branch and Bound with Underestimation Search")
print search.branch_and_bound_with_underestimation_graph_search(cn, cn.h).path()
print "Se expanden: " + str(search.get_nexpandnodes())

print('\n')

print("De la ciudad N a la ciudad T")
print("Branch and Bound Search")
print search.branch_and_bound_graph_search(nt).path()
print "Se expanden: " + str(search.get_nexpandnodes())

print('\n')

print("Branch and Bound with Underestimation Search")
print search.branch_and_bound_with_underestimation_graph_search(nt, nt.h).path()
print "Se expanden: " + str(search.get_nexpandnodes())

print('\n')

print("De la ciudad E a la ciudad O")
print("Branch and Bound Search")
print search.branch_and_bound_graph_search(eo).path()
print "Se expanden: " + str(search.get_nexpandnodes())

print('\n')

print("Branch and Bound with Underestimation Search")
print search.branch_and_bound_with_underestimation_graph_search(eo, eo.h).path()
print "Se expanden: " + str(search.get_nexpandnodes())

print('\n')

print("De la ciudad Z a la ciudad V")
print("Branch and Bound Search")
print search.branch_and_bound_graph_search(zv).path()
print "Se expanden: " + str(search.get_nexpandnodes())

print('\n')

print("Branch and Bound with Underestimation Search")
print search.branch_and_bound_with_underestimation_graph_search(zv, zv.h).path()
print "Se expanden: " + str(search.get_nexpandnodes())

print('\n')

#print("Branch and Bound Search Using Priority Queue")
#print search.branch_and_bound_graph_search2(ab).path()

#print search.astar_search(ab, ab.h).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

