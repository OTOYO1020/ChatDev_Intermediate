'''
Graph class to represent cities and roads, and to count distinct shortest paths.
'''
from collections import defaultdict, deque
from typing import List, Tuple
MOD = 10**9 + 7
class Graph:
    def __init__(self, n: int):
        self.n = n
        self.adj_list = defaultdict(list)
    def add_road(self, u: int, v: int):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    def count_paths(self, start: int, end: int) -> int:
        # Handle edge cases
        if self.n == 0:  # No cities
            return 0
        if self.n == 1:  # Only one city
            return 1
        if start == end:  # Start and end are the same
            return 1
        if len(self.adj_list[start]) == 0:  # Check if there are no roads from the start city
            return 0
        if not self.adj_list:  # No roads at all
            return 0
        queue = deque([start])
        distances = {i: float('inf') for i in range(1, self.n + 1)}
        distances[start] = 0
        path_count = {i: 0 for i in range(1, self.n + 1)}
        path_count[start] = 1
        while queue:
            current = queue.popleft()
            for neighbor in self.adj_list[current]:
                if distances[neighbor] == float('inf'):  # Not visited
                    distances[neighbor] = distances[current] + 1
                    queue.append(neighbor)
                if distances[neighbor] == distances[current] + 1:
                    path_count[neighbor] = (path_count[neighbor] + path_count[current]) % MOD
        # If the end city is unreachable, return 0
        return path_count[end] if distances[end] != float('inf') else 0