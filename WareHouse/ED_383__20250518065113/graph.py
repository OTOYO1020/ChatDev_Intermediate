'''
Graph class to represent the graph and compute minimum path weights.
'''
import heapq
from typing import List, Tuple
class Graph:
    def __init__(self, n: int):
        self.adj_list = {i: [] for i in range(n)}  # Initialize adjacency list for n vertices
    def add_edge(self, u: int, v: int, weight: int):
        self.adj_list[u].append((v, weight))  # Add edge from u to v
        self.adj_list[v].append((u, weight))  # Add edge from v to u (undirected graph)
    def f(self, x: int, y: int) -> int:
        if x == y:  # Check if the source and destination are the same
            return 0  # Return 0 cost if no traversal is needed
        min_heap = [(0, x)]  # (cost, vertex)
        distances = {i: float('inf') for i in self.adj_list}  # Initialize distances
        distances[x] = 0  # Distance to source is 0
        while min_heap:
            current_cost, current_vertex = heapq.heappop(min_heap)
            if current_vertex == y:
                return current_cost  # Return cost if destination is reached
            for neighbor, weight in self.adj_list[current_vertex]:
                new_cost = current_cost + weight
                if new_cost < distances[neighbor]:  # Update if a shorter path is found
                    distances[neighbor] = new_cost
                    heapq.heappush(min_heap, (new_cost, neighbor))
        return float('inf')  # Return inf if y is not reachable from x