import unittest
from graph import *


class GraphTestCase(unittest.TestCase):
    def test_graph(self):
        g = Graph([(0, 1), (1, 2), (0, 3), (2, 3), (3, 4), (4, 1), (4, 5)], [0], [0] * 6)
        self.assertEqual(g.neighbors(0), [1, 3])
        self.assertEqual(g.outdegree(0), 2)
        self.assertEqual(g.outdegree(5), 0)
        visited = []

        def p(n):
            visited.append(n)

        g.dfs(p, 0)
        self.assertEqual(visited, range(6))

    def test_subgraph(self):
        graph1 = Graph([(0, 1), (0, 2), (1, 3), (1, 4), (4, 2)], [0], [1]*5)
        self.assertEqual(1, subgraph_isomorphism(graph1, 0, graph1, 0))
        self.assertEqual(0, subgraph_isomorphism(graph1, 0, graph1, 1))

        graph2 = Graph([(0, 1), (0, 2), (1, 3), (1, 4), (4, 1)], [0], [1]*5)
        self.assertEqual(0, subgraph_isomorphism(graph1, 0, graph2, 0))

        graph3 = Graph([(0, 1), (1, 2), (0, 3), (2, 3), (3, 4), (4, 1), (4, 5)], [0], [0] * 6)
        self.assertEqual(1, subgraph_isomorphism(graph3, 0, graph3, 0))

if __name__ == '__main__':
    unittest.main()
