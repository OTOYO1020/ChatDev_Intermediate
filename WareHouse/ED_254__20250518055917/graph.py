'''
Graph class that represents the graph and implements BFS for query handling.
'''
from collections import deque, defaultdict
from typing import List, Tuple
class Graph:
    def __init__(self, N: int, edges: List[Tuple[int, int]]):
        self.N = N
        self.adj_list = defaultdict(list)
        self.degree = defaultdict(int)  # Track the degree of each vertex
        for u, v in edges:
            if self.degree[u] < 3 and self.degree[v] < 3:
                self.adj_list[u].append(v)
                self.adj_list[v].append(u)
                self.degree[u] += 1
                self.degree[v] += 1
            else:
                print(f"Skipping edge ({u}, {v}) as it exceeds vertex degree limit.")
    def bfs(self, start: int, k: int) -> List[int]:
        if k < 0:
            return []  # Return empty if k is negative
        visited = set()
        queue = deque([(start, 0)])  # (current_vertex, current_distance)
        visited.add(start)
        result = []
        # Handle isolated vertex case
        if start not in self.adj_list:
            return [start] if k >= 0 else []
        while queue:
            current, distance = queue.popleft()
            if distance <= k:  # Include current vertex if distance is less than or equal to k
                result.append(current)
                for neighbor in self.adj_list[current]:
                    if neighbor not in visited and distance + 1 <= k:  # Only enqueue if not visited and within distance
                        visited.add(neighbor)
                        queue.append((neighbor, distance + 1))
        return result
    def sum_of_indices(self, Q: int, queries: List[Tuple[int, int]]) -> List[int]:
        results = []
        for x, k in queries:
            vertices_within_k = self.bfs(x, k)
            results.append(sum(vertices_within_k))
        return results