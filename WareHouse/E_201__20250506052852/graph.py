'''
Graph representation and XOR distance calculation for a weighted tree.
'''
class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n + 1)]
        self.xor_dist = [0] * (n + 1)
    def add_edge(self, u, v, w):
        # Add an edge to the graph
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))
    def dfs(self, x, parent):
        # Perform DFS to compute XOR distances from vertex x
        for neighbor, weight in self.graph[x]:
            if neighbor != parent:
                self.xor_dist[neighbor] = self.xor_dist[x] ^ weight
                self.dfs(neighbor, x)  # Recursive DFS call
    def calculate_total_xor_distance(self):
        total_sum = 0
        # Store all xor_dist results for each vertex
        all_xor_dists = []
        for i in range(1, self.n + 1):
            self.xor_dist = [0] * (self.n + 1)  # Reset xor_dist for each DFS
            self.dfs(i, -1)  # Compute XOR distances from vertex i
            all_xor_dists.append(self.xor_dist)  # Store the result
        # Now calculate the total distance using stored results
        for i in range(1, self.n + 1):
            for j in range(i + 1, self.n + 1):  # Start from i + 1 to avoid redundant checks
                # Calculate distance using stored XOR distances
                distance = all_xor_dists[i - 1][j] ^ all_xor_dists[i - 1][i]
                total_sum += distance
        return total_sum % (10**9 + 7)