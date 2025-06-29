'''
Module to define the Graph class for representing an undirected graph.
'''
class Graph:
    def __init__(self, n):
        # Initialize adjacency list with n + 1 to accommodate 1-indexed vertices
        self.adjacency_list = [[] for _ in range(n + 1)]
    def add_edge(self, u, v):
        # Add edges for 1-indexed vertices, ensuring uniqueness and no self-loops
        if u != v:  # Prevent self-loops
            if v not in self.adjacency_list[u]:  # Check if the edge already exists
                self.adjacency_list[u].append(v)
            if u not in self.adjacency_list[v]:  # Check if the edge already exists
                self.adjacency_list[v].append(u)