import unittest
from graph import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        g = Graph([(0, 1), (1, 2), (0, 3), (2, 3), (3, 4), (4, 1)], [0], [0]*5)
        visited = []
        def p(n):
            visited.append(n)
        g.dfs(p, 0)
        print visited
        self.assertEqual(visited, range(5))




if __name__ == '__main__':
    unittest.main()
