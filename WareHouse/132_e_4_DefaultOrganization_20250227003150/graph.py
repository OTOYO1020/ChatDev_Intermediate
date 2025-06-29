'''
Graph class that manages the graph structure and performs BFS to find the shortest path.
'''
from collections import deque, defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = defaultdict(list)
    def add_edge(self, u, v):
        # Create edges for the three-layer structure
        for i in range(3):
            self.adj[(u, i)].append((v, (i + 1) % 3))
            self.adj[(v, i)].append((u, (i + 1) % 3))
    def bfs(self, start, target):
        queue = deque([(start, 0)])  # Start from (S, 0)
        visited = set()
        while queue:
            current, distance = queue.popleft()
            if current == (target, 0):
                return distance  # Return the distance directly
            if current not in visited:
                visited.add(current)
                for neighbor in self.adj[current]:
                    if neighbor not in visited:  # Check if neighbor is not visited
                        queue.append((neighbor, distance + 1))  # Increment distance for each step
        return -1