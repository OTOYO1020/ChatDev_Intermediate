'''
Module to define the Graph class and its methods for graph representation and coloring.
'''
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]
        self.colors = [-1] * vertices  # -1 means uncolored
    def add_edge(self, u, v, w):
        self.adjacency_list[u].append((v, w))
        self.adjacency_list[v].append((u, w))
    def color_graph(self):
        # Iterate through all vertices to ensure all components are colored
        for vertex in range(self.vertices):
            if self.colors[vertex] == -1:  # If the vertex is not colored
                self.colors[vertex] = 0  # Start coloring from this vertex
                self.dfs(vertex)  # Perform DFS to color connected component
    def dfs(self, vertex):
        for neighbor, weight in self.adjacency_list[vertex]:
            if self.colors[neighbor] == -1:  # If not colored
                if weight % 2 == 0:
                    self.colors[neighbor] = self.colors[vertex]  # Same color
                else:
                    self.colors[neighbor] = 1 - self.colors[vertex]  # Opposite color
                self.dfs(neighbor)