'''
Module to represent the graph and compute the minimum spanning tree.
'''
from typing import List, Tuple
class Graph:
    def __init__(self, N: int):
        self.V = N
        self.edges = []
        self.adj_list = {i: [] for i in range(N)}
    def add_edge(self, u: int, v: int, w: int):
        '''
        Adds an edge to the graph.
        '''
        self.edges.append((w, u, v))
        self.adj_list[u].append((v, w))
        self.adj_list[v].append((u, w))
    def find_parent(self, parent: List[int], i: int) -> int:
        '''
        Finds the parent of a node in the union-find structure.
        '''
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])
    def union(self, parent: List[int], rank: List[int], x: int, y: int):
        '''
        Unites two subsets in the union-find structure.
        '''
        xroot = self.find_parent(parent, x)
        yroot = self.find_parent(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
    def kruskal_mst(self) -> List[Tuple[int, int, int]]:
        '''
        Computes the minimum spanning tree using Kruskal's algorithm.
        '''
        result = []
        self.edges.sort()
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        for w, u, v in self.edges:
            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)
            if x != y:
                result.append((min(u, v), max(u, v), w))  # Store edges in a consistent format
                self.union(parent, rank, x, y)
        return result  # Return only the edges of the MST