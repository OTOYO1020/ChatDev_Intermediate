'''
Graph class to represent the graph and perform BFS.
'''
from collections import deque
class Graph:
    def __init__(self, N: int):
        self.N = N
        self.adj_list = [[] for _ in range(N)]
    def add_edge(self, u: int, v: int):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    def bfs(self):
        all_distances = []
        for start in range(self.N):
            distances = [-1] * self.N
            distances[start] = 0  # Set the distance to itself as 0
            queue = deque([start])
            while queue:
                current = queue.popleft()
                for neighbor in self.adj_list[current]:
                    if distances[neighbor] == -1:  # Not visited
                        distances[neighbor] = distances[current] + 1
                        queue.append(neighbor)
            all_distances.append(distances)
        return all_distances