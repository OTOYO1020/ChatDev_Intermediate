'''
Graph class to represent the graph and perform BFS for shortest path calculation.
'''
from collections import deque, defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = defaultdict(list)
    def add_edge(self, u, v):
        self.adj[u].append(v)
    def bfs(self, start, target):
        queue = deque([start])
        visited = set([start])
        distance = {start: 0}
        while queue:
            current = queue.popleft()
            if current == target:
                return distance[current] // 3  # Return distance divided by 3
            for neighbor in self.adj[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    distance[neighbor] = distance[current] + 1
                    queue.append(neighbor)
        return -1  # If target is not reachable