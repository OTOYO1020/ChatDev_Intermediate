'''
Module to define the Graph class for representing an undirected graph.
'''
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {i: [] for i in range(1, vertices + 1)}
    def add_edge(self, u: int, v: int):
        if u < 1 or u > self.vertices or v < 1 or v > self.vertices:
            raise ValueError(f"Invalid vertices: {u}, {v}. Must be between 1 and {self.vertices}.")
        if v not in self.graph[u]:  # Check if the edge already exists
            self.graph[u].append(v)
        if u not in self.graph[v]:  # Check if the edge already exists
            self.graph[v].append(u)
    def get_connected_vertices(self, v: int):
        if v < 1 or v > self.vertices:
            raise ValueError(f"Invalid vertex: {v}. Must be between 1 and {self.vertices}.")
        return self.graph[v]