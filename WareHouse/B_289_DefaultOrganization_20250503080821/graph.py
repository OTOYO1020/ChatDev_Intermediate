'''
Module to define the Graph class for managing the undirected graph.
'''
from collections import defaultdict, deque
class Graph:
    def __init__(self, n):
        '''
        Initializes the graph with n vertices.
        '''
        self.n = n
        self.adj_list = defaultdict(list)
    def add_edge(self, u, v):
        '''
        Adds an edge between vertices u and v, ensuring they are within bounds.
        '''
        if u < 1 or u > self.n or v < 1 or v > self.n:
            raise ValueError(f"Vertices {u} and {v} must be between 1 and {self.n}.")
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    def get_connected_component(self, start):
        '''
        Returns the connected component containing the vertex start using BFS.
        '''
        visited = set()
        queue = deque([start])
        component = []
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                component.append(vertex)
                for neighbor in self.adj_list[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return component