'''
Graph class to handle the transformation and BFS search.
'''
from collections import deque, defaultdict
class Graph:
    def __init__(self, N):
        self.N = N
        self.edges = defaultdict(list)
    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)
    def transform_graph(self):
        transformed_edges = defaultdict(list)
        for u in self.edges:
            for v in self.edges[u]:
                for i in range(3):
                    transformed_edges[(u, i)].append((v, (i + 1) % 3))
                    transformed_edges[(v, i)].append((u, (i + 1) % 3))
        return transformed_edges
    def bfs(self, S, T):
        transformed_edges = self.transform_graph()
        queue = deque([(S, 0)])
        visited = set()
        visited.add((S, 0))
        distance = 0
        while queue:
            for _ in range(len(queue)):
                current_node = queue.popleft()
                if current_node == (T, 0):
                    return distance // 3
                for neighbor in transformed_edges[current_node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            distance += 1
        return -1