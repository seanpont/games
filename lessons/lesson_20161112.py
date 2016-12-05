"""
Algorithms And Data Structures







Introduction to Graph Theory

Can be used to model maps, web content, circuits, schedules, friends...

Vertices (also called Nodes)
Edges: Connect two vertices
  Can be Directed or Undirected (bidirectional)
Path: Sequence of Vertices connected by edges

Text Adventure Game!
(like the website)

Case Study: Union Find

Define class UnionFind:
  initializer: should take the size
  functions:
    union(p, q): adds an edge between p and q
    connected(p, q): returns true if p and q are connected
  later, we can develop two additional functions:
    component(p): returns an integer identifier for p's component (ie the set)
    component_count(): return the number of components

Solving this problem means thinking about the data structure and the algorithm
we will apply to it. They are interconnected. For each algorithm that we
develop, we will analyze its space and time efficiency.

Notes:
  quick-find: array of size N, connected if same component
  quick-union:
"""