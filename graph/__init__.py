import random as r
import functional as f
from itertools import permutations


def make_adjacency_list(from_nodes, to_nodes, num_edges):
    return [(r.choice(from_nodes), r.choice(to_nodes))
            for _ in xrange(num_edges)]


class Graph(object):
    def __init__(self, adj_list, entry_nodes, node_flavors):
        self.adj_list = adj_list
        self.adj_index = f.group_by(adj_list, lambda x: x[0], lambda x: x[1])
        self.entry_nodes = entry_nodes
        self.node_flavors = node_flavors

    def neighbors(self, node):
        return self.adj_index.get(node, ())

    def outdegree(self, node):
        return len(self.neighbors(node))

    def dfs(self, fn, node, visited=None):
        """
        Apply function fn to each node using a depth-first search, starting at node
        :param fn: The function to apply to each node
        :param node: The node to start at
        :param visited: nodes already visited, or None
        """
        # Add the node to the visited set
        visited = f.add(f.ifNone(visited, set), node)
        fn(node)
        for neighbor in self.neighbors(node):
            if neighbor not in visited:
                self.dfs(fn, neighbor, visited)


def subgraph_isomorphism(graph1, node1, graph2, node2,
                         flavor_comparator_fn=lambda f1, f2: 1 if f1 == f2 else 0,
                         cache=None, visited=None):
    """
    Returns an integer [0, 1] that describes how isomorphic two
    sub-graphs are. Does not return a boolean because this method can take into
    account a certain amount of slop (mismatched flavors, inlined functions that
    amount to missing nodes in one graph or the other.
    :param graph1: Graph
    :type graph1: Graph
    :param node1: a node
    :param graph2: Graph
    :type graph2: Graph
    :param node2: a node
    :param flavor_comparator_fn: A function to compare two flavors.
    Should return > 0 if they are reasonably close
    :param cache: cheat sheet.
    :type cache: dict
    :param visited: a set of node pairs that have been visited
    :type visited: set
    :return: How isomorphic two subraphs rooted at node1 and node2 are,
    based on their flavor
    """
    nodes = (node1, node2)

    visited = f.ifNone(visited, set)
    if nodes in visited:
        print "cycle detected"
        return 1
    visited.add(nodes)

    cache = f.ifNone(cache, dict)
    if nodes in cache:
        return cache[nodes]

    flavor_diff = flavor_comparator_fn(graph1.node_flavors[node1], graph2.node_flavors[node2])
    if flavor_diff == 0:
        return 0

    # TODO: accommodate skipped nodes (inlined functions)
    if graph1.outdegree(node1) != graph2.outdegree(node2):
        return 0

    if graph1.outdegree(node1) == 0:
        print "isomorphism of", node1, node2, ":", flavor_diff
        cache[nodes] = flavor_diff
        return flavor_diff

    # TODO: apply some magic heuristic to avoid proceeding if at all possible
    # because it's about to get ugly.
    # Examples: Sum of flavors of children, size of sub-graph, etc.

    child_isomorphisms = []
    for neighbors1 in permutations(graph1.neighbors(node1)):
        for neighbors2 in permutations(graph2.neighbors(node2)):
            child_isomorphism = 1
            for neighbor1, neighbor2 in zip(neighbors1, neighbors2):
                child_isomorphism *= subgraph_isomorphism(
                    graph1, neighbor1, graph2, neighbor2, flavor_comparator_fn, cache, visited)
                if child_isomorphism == 0:
                    break
            child_isomorphisms.append(child_isomorphism)

    isomorphism = flavor_diff * max(child_isomorphisms)

    print "isomorphism of", node1, node2, ":", isomorphism
    cache[nodes] = isomorphism
    return isomorphism


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
