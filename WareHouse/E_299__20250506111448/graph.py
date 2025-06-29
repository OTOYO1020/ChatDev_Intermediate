'''
Graph class to represent an undirected graph using an adjacency list.
'''
from collections import deque, defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def bfs(self, starts):
        distances = {vertex: float('inf') for vertex in self.graph.keys()}
        queue = deque(starts)
        for start in starts:
            distances[start] = 0  # Start painting these vertices black
        while queue:
            current = queue.popleft()
            for neighbor in self.graph[current]:
                if distances[neighbor] == float('inf'):  # Not visited
                    distances[neighbor] = distances[current] + 1
                    queue.append(neighbor)
        return distances  # Return distances