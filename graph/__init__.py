import random as r
import functional as f
from itertools import permutations
from collections import namedtuple
set = frozenset


def make_adjacency_list(from_nodes, to_nodes, num_edges):
    return [(r.choice(from_nodes), r.choice(to_nodes))
            for _ in xrange(num_edges)]


class Graph(object):
    def __init__(self, adj_list, entry_nodes, node_flavors):
        self.adj_list = adj_list
        self.adj_index = {n: set(adj) for n, adj in
                          (f.group_by(adj_list, lambda x: x[0], lambda x: x[1])).iteritems()}
        self.entry_nodes = entry_nodes
        self.node_flavors = node_flavors

    def neighbors(self, node):
        return self.adj_index.get(node, set())

    def outdegree(self, node):
        return len(self.neighbors(node))

    def dfs(self, node, visited=None):
        """
        Returns an iterator over the graph starting at node
        """
        # Add the node to the visited set
        visited = f.add(f.ifNone(visited, set), node)
        yield node
        for neighbor in self.neighbors(node):
            if neighbor not in visited:
                for child in self.dfs(neighbor, visited):
                    yield child

    def flavor(self, node):
        return self.node_flavors[node]


def isomorphic(graph1, node1, graph2, node2,
               flavor_comparator_fn=lambda f1, f2: f1==f2):
    node_comp_fn = lambda n1, n2: flavor_comparator_fn(graph1[n1], graph2[n2])
    return _isomorphic(graph1, node1, graph2, node2, node_comp_fn)

def _isomorphic(graph1, node1, graph2, node2, node_comp_fn):
    """
    Returns an integer [0, 1] that describes how isomorphic two
    sub-graphs are. Does not return a boolean because this method can take into
    account a certain amount of slop (mismatched flavors, inlined functions that
    amount to missing nodes in one graph or the other.
    :type graph1: Graph
    :type node1: int
    :type graph2: Graph
    :type node2: int
    :type flavor_fn: function
    :rtype bool
    """
    if not node_comp_fn(node1, node2):
        return False
    graph1_nodes = [n for n in graph1.dfs(node1)]
    # constraints_stack is a list of tuples (constraints generator, graph1_nodes index)
    # constraints is a map from graph1 nodes to graph2 nodes
    constraints_stack = [(({node1: node2},), 0)]
    while constraints_stack:
        constraints_gen, graph1_node_index = constraints_stack.pop()
        for constraints in constraints_gen:
            graph1_node = graph1_nodes[graph1_node_index]
            graph2_node = constraints[graph1_node]
            neighbors1 = graph1.neighbors(graph1_node)
            neighbors2 = graph2.neighbors(graph2_node)

            # Check if any constraints have been broken
            known_neighbors_1 = neighbors1 & set(constraints.keys())
            known_neighbors_2 = neighbors2 & set(constraints.values())
            if known_neighbors_2 != set([constraints[n] for n in known_neighbors_1]):
                print "constraint violation detected"
                continue
            unknown_neighbors_1 = tuple(neighbors1 - known_neighbors_1)
            unknown_neighbors_2 = tuple(neighbors2 - known_neighbors_2)

            # Four possibilities:
            # There are no 1s and 2s
            # There are more 1s than 2s
            # There are equal 1s and 2s
            # There are less 1s than 2s

            if len(unknown_neighbors_1) == 0 and len(unknown_neighbors_2) == 0:
                constraints_stack.append(((constraints,), graph1_node_index + 1))

            for ordered_neighbors2 in permutations(unknown_neighbors_2):
                # check flavors to see if valid match-up
                node_pairs = zip(unknown_neighbors_1, ordered_neighbors2)
                if all((node_comp_fn(n1, n2) for n1, n2 in node_pairs)):
                    new_constraints = constraints.copy()
                    new_constraints.update({n1: n2 for n1, n2 in node_pairs})
                    constraints_stack.append((new_constraints, graph1_node_index + 1))






def label_library_nodes(full_graph, library_graph):
    """
    Explore the graph and return a map that labels all nodes in the graph
    as either in the library or not
    """
    labels = {}
    entry_point = full_graph.entry_nodes[0]

    def label_nodes(node):
        pass

    full_graph.dfs(label_nodes, entry_point)
    return labels


def solve(num_library_nodes=1000,
          num_library_edges=3000,
          num_library_entry_points=100,
          num_program_nodes=100,
          num_program_edges=400,
          num_program_library_edges=100,
          num_node_flavors=20):
    # Each node represents a function
    num_nodes = num_library_nodes + num_program_nodes
    all_nodes = range(0, num_nodes)

    # Create a cyclic graph containing all the library nodes
    library_nodes = all_nodes[:num_library_nodes]
    library_adj_list = make_adjacency_list(
        library_nodes, library_nodes, num_library_edges)

    # Create a cyclic graph representing the portion of the program that
    # does not call into the library
    program_nodes = all_nodes[num_library_nodes:]
    program_adj_list = make_adjacency_list(
        program_nodes, program_nodes, num_program_edges)
    # The program only has one entry point.
    program_entry_point = program_nodes[0]

    # Create the call graph that links the program to the library.
    program_library_adj_list = make_adjacency_list(
        program_nodes, library_nodes, num_program_library_edges)

    # The library entry points contain all library nodes linked to from the
    # program as well as some that aren't
    library_entry_points = set(map(lambda x: x[1], program_library_adj_list))
    while len(library_entry_points) < num_library_entry_points:
        num_to_add = num_library_entry_points - len(library_entry_points)
        library_entry_points.update(
            [r.choice(library_nodes) for _ in xrange(num_to_add)])

    # The full graph is the union of all three sub-graphs
    full_adj_list = library_adj_list \
                    + program_adj_list \
                    + program_library_adj_list

    # All nodes have certain characteristics, like the number of instructions.
    # Assume that we have bucketed all nodes into n buckets, which we will
    # call flavors. It is assumed that the bucketing is rough enough to
    # accommodate variations in the number of instructions and such
    node_flavors = [r.randint(1, num_node_flavors) for _ in xrange(num_nodes)]

    # Create a copy of the library with different node labels but the same
    # call graph and node flavors.
    library_nodes_2 = [-1 * n - 1 for n in library_nodes]
    lib2_adj_list = [(library_nodes_2[n1], library_nodes_2[n2])
                     for n1, n2 in library_adj_list]
    lib2_entry_nodes = [library_nodes_2[n] for n in library_entry_points]
    lib2_node_flavors = {library_nodes_2[n]: node_flavors[n]
                         for n in library_nodes}

    full_graph = Graph(full_adj_list, [program_entry_point], node_flavors)
    library_graph = Graph(lib2_adj_list, lib2_entry_nodes, lib2_node_flavors)

    print "unfolding..."
    label_library_nodes(full_graph, library_graph)


if __name__ == '__main__':
    solve(num_library_nodes=10,
          num_library_edges=30,
          num_library_entry_points=5,
          num_program_nodes=10,
          num_program_edges=20,
          num_program_library_edges=3)
