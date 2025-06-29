'''
Graph class to represent an undirected graph using an adjacency list.
'''
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {i: set() for i in range(1, vertices + 1)}  # Use a set for faster lookups
    def add_edge(self, u, v):
        '''
        Add an edge between vertices u and v in both directions.
        '''
        self.graph[u].add(v)
        self.graph[v].add(u)
    def count_triangles(self):
        '''
        Count the number of triangles in the graph.
        A triangle is formed by three distinct vertices a, b, c such that
        there are edges (a, b), (b, c), and (c, a).
        '''
        count = 0
        # Iterate through each vertex
        for a in range(1, self.vertices + 1):
            neighbors = list(self.graph[a])  # Get neighbors of vertex a
            num_neighbors = len(neighbors)
            # Check pairs of neighbors to find triangles
            for i in range(num_neighbors):
                for j in range(i + 1, num_neighbors):
                    b = neighbors[i]
                    c = neighbors[j]
                    if b in self.graph[c]:  # Check if edge (b, c) exists
                        count += 1  # A triangle is found
        return count