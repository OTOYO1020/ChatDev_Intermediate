'''
Graph class to represent the graph and find the maximum score path.
'''
class Graph:
    def __init__(self, n, edges, values):
        self.n = n
        self.edges = edges
        self.values = values
        self.adj_list = {i: [] for i in range(1, n + 1)}
        self.build_graph()
    def build_graph(self):
        for u, v in self.edges:
            self.add_edge(u, v)
            self.add_edge(v, u)  # Assuming undirected graph
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
    def find_max_score_path(self):
        # Check if vertex N is reachable from vertex 1
        if not self.is_reachable(1, self.n):
            return 0
        max_score = [0]
        def dfs(node, path, visited):
            visited.add(node)  # Mark the node as visited
            path.append(node)
            if node == self.n:
                if self.is_non_decreasing(path):
                    score = len(set(self.values[v - 1] for v in path))  # Use values for scoring
                    max_score[0] = max(max_score[0], score)
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor, path, visited)
            path.pop()
            visited.remove(node)  # Unmark the node after exploring
        dfs(1, [], set())  # Initialize visited as an empty set for each DFS call
        return max_score[0]
    def is_reachable(self, start, end):
        visited = set()
        def dfs(node):
            if node == end:
                return True
            visited.add(node)
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False
        return dfs(start)
    def is_non_decreasing(self, path):
        return all(path[i] <= path[i + 1] for i in range(len(path) - 1))