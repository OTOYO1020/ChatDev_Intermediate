'''
Tree class to represent the tree structure and calculate distances.
'''
class Tree:
    def __init__(self, n):
        self.n = n
        self.adj = {i: [] for i in range(1, n + 1)}
        self.C = []
        self.subtree_size = [0] * (n + 1)
        self.depth = [0] * (n + 1)  # To store depth of each node
        self.parent = [-1] * (n + 1)  # To store parent information for LCA
        self.lift = [[-1] * 20 for _ in range(n + 1)]  # Binary lifting table
    def add_edge(self, a, b):
        self.adj[a].append(b)
        self.adj[b].append(a)
    def dfs(self, node, parent):
        self.depth[node] = 0 if parent == -1 else self.depth[parent] + 1  # Initialize depth for root node
        self.subtree_size[node] = 1
        self.parent[node] = parent
        self.lift[node][0] = parent  # 2^0-th ancestor
        for i in range(1, 20):
            if self.lift[node][i - 1] != -1:
                self.lift[node][i] = self.lift[self.lift[node][i - 1]][i - 1]
        for neighbor in self.adj[node]:
            if neighbor != parent:
                self.dfs(neighbor, node)
                self.subtree_size[node] += self.subtree_size[neighbor]
    def lca(self, a, b):
        if self.depth[a] < self.depth[b]:
            a, b = b, a  # Ensure a is deeper than b
        # Lift a to the same depth as b
        for i in range(19, -1, -1):
            if self.depth[self.lift[a][i]] >= self.depth[b]:
                a = self.lift[a][i]
        if a == b:
            return a
        # Lift both a and b until their parents match
        for i in range(19, -1, -1):
            if self.lift[a][i] != self.lift[b][i]:
                a = self.lift[a][i]
                b = self.lift[b][i]
        return self.parent[a]
    def calculate_distance(self, a, b):
        # Calculate distance using LCA
        return self.depth[a] + self.depth[b] - 2 * self.depth[self.lca(a, b)]
    def f(self, x):
        # Calculate f(x) using the calculate_distance method
        total_distance = 0
        for i in range(1, self.n + 1):
            total_distance += self.C[i - 1] * self.calculate_distance(x, i)
        return total_distance
    def calculate_f_values(self):
        f_values = [0] * (self.n + 1)
        # Calculate f(1) first
        f_values[1] = self.f(1)
        # Use DFS to calculate f(v) for all vertices
        def dfs_f(node, parent):
            for neighbor in self.adj[node]:
                if neighbor != parent:
                    # Calculate f(neighbor) based on f(node)
                    f_values[neighbor] = f_values[node] + (self.n - 2 * self.subtree_size[neighbor])
                    dfs_f(neighbor, node)
        dfs_f(1, -1)
        return f_values