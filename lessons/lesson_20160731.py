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


def draw_complex_network(rows, cols, network):
  master = Tk()

  def pos(x):
    return x * 10 + 10

  w = Canvas(master, width=pos(rows), height=pos(cols))
  w.pack()

  for row in range(rows):
    for col in range(cols):
      y, x = pos(row), pos(col)
      w.create_oval(x - 2, y - 2, x + 2, y + 2, fill='black')

  for edge in network:
    y1, x1, y2, x2 = edge
    w.create_line(pos(x1), pos(y1), pos(x2), pos(y2))

  mainloop()


if __name__ == '__main__':
  rows, cols, edges = 8, 8, 8 ** 2
  network = generate_network(rows, cols, edges)
  draw_complex_network(rows, cols, network)

  rows, cols, edges = 64, 64, 64**2
  network = generate_network(rows, cols, edges)
  draw_complex_network(rows, cols, network)
