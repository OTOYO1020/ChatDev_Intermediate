'''
Graph class to represent the graph structure and related operations.
'''
from itertools import combinations
from utils import nCr
class Graph:
    def __init__(self, N, edges):
        self.N = N
        self.edges = edges
        self.adjacency_list = self.create_adjacency_list()
        self.degree = self.calculate_degrees()
    def create_adjacency_list(self):
        adj_list = {i: [] for i in range(1, self.N + 1)}
        for u, v in self.edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        return adj_list
    def calculate_degrees(self):
        degree = {i: 0 for i in range(1, self.N + 1)}
        for u, v in self.edges:
            degree[u] += 1
            degree[v] += 1
        return degree
    def count_edges(self, red_count, blue_count):
        count = 0
        for u in range(1, self.N + 1):
            if u in red_count:
                for v in self.adjacency_list[u]:
                    if v in blue_count:
                        count += 1
        return count
    def count_valid_painting_ways(self, K):
        valid_count = 0
        all_vertices = list(range(1, self.N + 1))
        # Precompute combinations
        comb = [0] * (self.N + 1)
        for i in range(self.N + 1):
            comb[i] = nCr(self.N, i)
        # Efficiently count valid configurations
        for red_count in range(K + 1):
            blue_count = self.N - red_count
            edges_between = self.count_edges(red_count, blue_count)
            if edges_between % 2 == 0:
                valid_count += comb[red_count] * comb[blue_count]
        return valid_count % 998244353