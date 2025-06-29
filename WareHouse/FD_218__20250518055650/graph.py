'''
Contains the Graph and ShortestDistanceCalculator classes for handling graph operations.
'''
from collections import defaultdict, deque
from typing import List, Tuple
class Graph:
    def __init__(self, vertices: int):
        self.V = vertices
        self.adj_list = defaultdict(list)
    def add_edge(self, u: int, v: int):
        if v not in self.adj_list[u]:  # Avoid duplicates
            self.adj_list[u].append(v)
    def remove_edge(self, u: int, v: int):
        if v in self.adj_list[u]:  # Check if the edge exists before removing
            self.adj_list[u].remove(v)
    def bfs(self, start: int, end: int) -> int:
        if start == end:  # If start and end are the same, distance is 0
            return 0
        visited = [False] * (self.V + 1)
        queue = deque([start])
        distances = [float('inf')] * (self.V + 1)
        distances[start] = 0
        visited[start] = True
        while queue:
            current = queue.popleft()
            for neighbor in self.adj_list[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    distances[neighbor] = distances[current] + 1
                    queue.append(neighbor)
                    if neighbor == end:
                        return distances[neighbor]  # Return immediately if we reach the end vertex
        # If we exit the loop and haven't found the end vertex, return -1
        return -1 if distances[end] == float('inf') else distances[end]
class ShortestDistanceCalculator:
    def __init__(self, graph: Graph, edges: List[Tuple[int, int]]):
        self.graph = graph
        self.edges = edges  # Store the original edges
    def calculate_shortest_distances(self) -> List[int]:
        results = []
        # Handle the case where there are no edges or insufficient vertices
        if self.graph.V < 2 or len(self.edges) == 0:
            return [-1] * len(self.edges)  # Return a list of -1 for each edge removal attempt
        # Check if Vertex 1 can reach Vertex N initially
        initial_distance = self.graph.bfs(1, self.graph.V)
        if initial_distance == -1:
            return [-1] * len(self.edges)  # If unreachable, return -1 for all edges
        # Iterate over the original edges
        for u, v in self.edges:
            # Remove the edge (u, v)
            self.graph.remove_edge(u, v)
            # Calculate the shortest distance from Vertex 1 to Vertex N after removing the edge
            distance = self.graph.bfs(1, self.graph.V)
            results.append(distance)
            # Restore the edge (u, v)
            self.graph.add_edge(u, v)  # Ensure the edge is added back correctly
        return results