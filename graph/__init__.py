import random as r

import functional as f

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

    def adj(self, node):
        return self.adj_index.get(node, ())

    def outdegree(self, node):
        return len(self.adj(node))

    def dfs(self, node, visited=None):
        """
        Returns an iterator over the graph starting at node
        """
        # Add the node to the visited set
        visited = f.add(f.if_none(visited, set), node)
        yield node
        for neighbor in self.neighbors(node):
            if neighbor not in visited:
                for child in self.dfs(neighbor, visited):
                    yield child

    def flavor(self, node):
        return self.node_flavors[node]


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
    # label_library_nodes(full_graph, library_graph)


if __name__ == '__main__':
    solve(num_library_nodes=10,
          num_library_edges=30,
          num_library_entry_points=5,
          num_program_nodes=10,
          num_program_edges=20,
          num_program_library_edges=3)
