"""
Introduction to Graph Theory

Can be used to model maps, web content, circuits, schedules, friends...

Vertices (also called Nodes)
Edges: Connect two vertices
  Can be Directed or Undirected (bidirectional)
Path: Sequence of Vertices connected by edges
A Tree is an Acyclic connected graph
Depth-first search
  Recursive solution:
  To visit a vertex:
    mark vertex as having been visited
    visit (recursively) all adjacent vertices that have not yet been visited.
Breadth-first search
  Put source vertex in queue
  while queue is not empty:
    take vertex from queue and mark as visited
    put all unvisited adjacent vertices on queue


Text Adventure Game!

How could we find a 'solution' to the text adventure game automatically?
"""

