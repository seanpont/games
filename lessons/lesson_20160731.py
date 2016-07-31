"""
Finish RoShamBo

If there is time:

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

from Tkinter import *
import random


def generate_network(rows, cols, edges):
  conns = []
  for _ in range(edges):
    row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
    adj = [(row + r, col + c) for r, c in ((1, 0), (-1, 0), (0, 1), (0, -1))]
    adj = filter(lambda rc: 0 <= rc[0] < rows and 0 <= rc[1] < cols, adj)
    row1, col1 = random.choice(adj)
    conns.append((row, col, row1, col1))
  return conns


def pos(x):
  return x * 10 + 10


def draw_network(canvas, rows, cols, network):
  print 'draw network'
  canvas.delete("all")

  for row in range(rows):
    for col in range(cols):
      y, x = pos(row), pos(col)
      canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill='black')

  for edge in network:
    y1, x1, y2, x2 = edge
    canvas.create_line(pos(x1), pos(y1), pos(x2), pos(y2))


def show_network(rows, cols):
  master = Tk()
  canvas = Canvas(master, width=pos(rows), height=pos(cols))
  canvas.pack()

  def redraw():
    draw_network(canvas, rows, cols, generate_network(rows, cols, rows * cols))

  master.bind("r", lambda _: redraw())
  redraw()
  mainloop()


if __name__ == '__main__':
  show_network(8, 8)
  show_network(64, 64)
