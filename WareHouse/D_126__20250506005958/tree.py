'''
Module to represent the tree structure and manage edges.
'''
class Tree:
    def __init__(self, n):
        """
        Initializes the Tree with n vertices.
        Parameters:
        n (int): The number of vertices in the tree.
        """
        self.n = n
        self.adjacency_list = [[] for _ in range(n + 1)]
    def add_edge(self, u, v, w):
        """
        Adds an edge between vertices u and v with weight w.
        Parameters:
        u (int): One vertex of the edge.
        v (int): The other vertex of the edge.
        w (int): The weight of the edge (not used in coloring).
        """
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)
    def __getitem__(self, vertex):
        """
        Returns the adjacency list for the given vertex.
        Parameters:
        vertex (int): The vertex for which to get the adjacency list.
        Returns:
        list: The list of adjacent vertices.
        """
        return self.adjacency_list[vertex]