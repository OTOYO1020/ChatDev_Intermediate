'''
Graph class to represent the graph using an adjacency list.
'''
class Graph:
    def __init__(self, N):
        self.N = N
        self.adj_list = {i: [] for i in range(N)}
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    def connected_components(self):
        visited = [False] * self.N
        count = 0
        def dfs(v):
            visited[v] = True
            for neighbor in self.adj_list[v]:
                if not visited[neighbor]:
                    dfs(neighbor)
        for i in range(self.N):
            if not visited[i]:
                dfs(i)
                count += 1
        return count