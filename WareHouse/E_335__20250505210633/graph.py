'''
Module to represent an undirected graph using an adjacency list.
'''
class Graph:
    def __init__(self, vertices):
        self.graph = {i: [] for i in range(1, vertices + 1)}
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)