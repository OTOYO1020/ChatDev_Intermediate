'''
Graph class to represent the graph structure and handle edge storage.
'''
from itertools import combinations
class Graph:
    def __init__(self, n):
        self.n = n  # Number of vertices
        self.adj_list = [[] for _ in range(n)]  # Adjacency list to store edges
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # Since the graph is undirected
    def count_ways(self, k):
        count_ways = 0
        # Iterate over all combinations of N vertices to select K vertices to paint red
        for red_vertices in combinations(range(self.n), k):
            red_set = set(red_vertices)
            edge_count_red_blue = 0  # Counter for edges connecting red and blue vertices
            # Count edges connecting red and blue vertices
            for u in red_vertices:
                for v in self.adj_list[u]:
                    if v not in red_set:  # Check if v is a blue vertex
                        edge_count_red_blue += 1
            # Since each edge is counted twice (once from each vertex), divide by 2
            edge_count_red_blue //= 2
            # Check if the count of edges connecting different colors is even
            if edge_count_red_blue % 2 == 0:
                count_ways += 1
        return count_ways % 998244353