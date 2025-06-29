'''
Module for tree construction and query handling.
'''
from typing import List, Tuple
import heapq
class Tree:
    def __init__(self, N: int, edges: List[Tuple[int, int]], values: List[int]):
        self.N = N
        self.edges = edges
        self.values = values
        self.adj_list = [[] for _ in range(N)]
        self.build_tree()
    def build_tree(self):
        for u, v in self.edges:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
    def dfs(self, node: int, visited: List[bool], collected_values: List[int]):
        visited[node] = True
        collected_values.append(self.values[node])
        for neighbor in self.adj_list[node]:
            if not visited[neighbor]:  # Only check if the neighbor is not visited
                self.dfs(neighbor, visited, collected_values)
    def find_kth_largest_in_subtree(self, V: int, K: int) -> int:
        visited = [False] * self.N
        collected_values = []
        self.dfs(V, visited, collected_values)
        # Use a min-heap to find the K-th largest element
        if len(collected_values) < K:
            raise ValueError("K is larger than the number of vertices in the subtree.")
        min_heap = []
        for value in collected_values:
            heapq.heappush(min_heap, value)
            if len(min_heap) > K:
                heapq.heappop(min_heap)
        return min_heap[-1]  # Return the K-th largest value