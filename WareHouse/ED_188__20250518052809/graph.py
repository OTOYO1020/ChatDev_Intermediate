'''
Graph representation for towns and roads.
'''
class Graph:
    def __init__(self, n):
        self.n = n
        self.adj_list = {i: [] for i in range(1, n + 1)}  # Keep 1-based indexing
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
    def dfs(self, start, visited):
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                for neighbor in self.adj_list[node]:
                    stack.append(neighbor)