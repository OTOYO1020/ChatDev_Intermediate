'''
Handles input validation for the Tree Coloring application.
'''
from typing import List, Tuple
from collections import defaultdict
class InputValidation:
    @staticmethod
    def validate_edges(N: int, edges: List[Tuple[int, int, int]]) -> bool:
        if len(edges) != N - 1:
            return False
        seen_edges = set()
        for u, v, w in edges:
            if not (1 <= u <= N and 1 <= v <= N and w > 0):
                return False
            if u == v or (u, v) in seen_edges or (v, u) in seen_edges:
                return False  # Check for self-loops and duplicate edges
            seen_edges.add((u, v))
        return True
    @staticmethod
    def is_connected(N: int, edges: List[Tuple[int, int, int]]) -> bool:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [False] * (N + 1)
        def dfs(vertex):
            visited[vertex] = True
            for neighbor in graph[vertex]:
                if not visited[neighbor]:
                    dfs(neighbor)
        dfs(1)  # Start DFS from vertex 1
        return all(visited[1:N + 1])  # Check if all vertices are visited