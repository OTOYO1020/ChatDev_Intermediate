'''
Graph class to represent the graph and calculate minimum path weights.
'''
import heapq
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = {i: [] for i in range(vertices)}
    def add_edge(self, u, v, w):
        # Adjust for 1-based indexing
        self.edges[u - 1].append((v - 1, w))
        self.edges[v - 1].append((u - 1, w))  # Assuming undirected graph
    def f(self, x, y):
        # Adjust for 1-based indexing
        x -= 1
        y -= 1
        # Raise an error if x or y is out of bounds
        if x < 0 or x >= self.vertices or y < 0 or y >= self.vertices:
            raise ValueError(f"Vertices {x + 1} and {y + 1} must be within the range 1 to {self.vertices}.")
        # Return 0 if the source and destination are the same
        if x == y:
            return 0
        # Dijkstra's algorithm
        min_heap = [(0, x)]  # Adjust for 0-based indexing
        distances = {i: float('inf') for i in range(self.vertices)}
        distances[x] = 0  # Adjust for 0-based indexing
        while min_heap:
            current_distance, current_vertex = heapq.heappop(min_heap)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in self.edges[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))
        # Check if a path exists
        if distances[y] == float('inf'):
            return float('inf')  # Return inf if no path exists
        return distances[y]