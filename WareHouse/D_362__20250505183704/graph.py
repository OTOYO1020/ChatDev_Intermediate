'''
Module to define the Graph class and implement Dijkstra's algorithm.
'''
import heapq
class Graph:
    def __init__(self, vertices, weights):
        self.V = vertices
        self.A = weights  # Store vertex weights
        self.adj_list = {i: [] for i in range(1, vertices + 1)}
    def add_edge(self, u, v, weight):
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))  # Assuming undirected graph
    def dijkstra(self, start):
        min_heap = [(self.A[start - 1], start)]  # (distance, vertex)
        distances = {i: float('inf') for i in range(1, self.V + 1)}
        distances[start] = self.A[start - 1]  # Initialize with the weight of the starting vertex
        visited = set()  # Track visited vertices
        while min_heap:
            current_distance, current_vertex = heapq.heappop(min_heap)
            if current_vertex in visited:
                continue
            visited.add(current_vertex)  # Mark the vertex as visited
            for neighbor, weight in self.adj_list[current_vertex]:
                distance = current_distance + weight + self.A[neighbor - 1]  # Include the weight of the neighbor vertex
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))
        return distances