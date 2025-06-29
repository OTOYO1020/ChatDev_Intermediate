'''
Graph class to represent an undirected graph and perform queries.
'''
from collections import deque
class Graph:
    def __init__(self, vertices):
        if vertices <= 0:
            raise ValueError("Number of vertices must be a positive integer.")
        self.vertices = vertices
        self.graph = {i: [] for i in range(1, vertices + 1)}  # Adjusted for 1-based indexing
    def add_edge(self, a, b):
        if a < 1 or a > self.vertices or b < 1 or b > self.vertices:
            raise ValueError("Vertex indices must be within the range of the number of vertices.")
        if len(self.graph[a]) < 3 and len(self.graph[b]) < 3:  # Maximum degree of 3
            self.graph[a].append(b)
            self.graph[b].append(a)
        else:
            raise ValueError(f"Cannot add edge ({a}, {b}): Maximum degree exceeded.")
    def sum_of_indices_within_distance(self, x, k):
        if x < 1 or x > self.vertices:
            raise ValueError("Query vertex must be within the range of the number of vertices.")
        if k == 0:
            return x  # Return the index of the starting vertex only if distance is 0
        if not self.graph[x]:  # Check if the starting vertex has no neighbors
            return 0  # If no neighbors and k > 0, return 0 instead of the vertex itself
        visited = set()
        queue = deque([(x, 0)])  # (current vertex, current distance)
        total_sum = 0
        while queue:
            current, distance = queue.popleft()
            if current not in visited:  # Check for visited vertices
                visited.add(current)
                total_sum += current  # Accumulate the sum of indices
                if distance < k:
                    for neighbor in self.graph[current]:
                        if neighbor not in visited:
                            queue.append((neighbor, distance + 1))  # Enqueue neighbor
        return total_sum