'''
Contains the GraphCycleDetector class for detecting cycles in a directed graph.
'''
class GraphCycleDetector:
    def __init__(self, N, M, edges):
        self.N = N
        self.M = M
        self.edges = edges
        self.adj_list = self.build_adjacency_list()
        self.visited = [False] * (N + 1)
        self.rec_stack = [False] * (N + 1)
        self.min_cycle_length = float('inf')
    def build_adjacency_list(self):
        adj_list = {i: [] for i in range(1, self.N + 1)}
        for u, v in self.edges:
            adj_list[u].append(v)
        return adj_list
    def dfs(self, v, current_path):
        self.visited[v] = True
        self.rec_stack[v] = True
        current_path.append(v)  # Use a list to maintain the order of the path
        for neighbor in self.adj_list[v]:
            if not self.visited[neighbor]:
                self.dfs(neighbor, current_path)  # Continue DFS without edge count
            elif self.rec_stack[neighbor]:  # Cycle detected
                if 1 in current_path:  # Check if cycle includes vertex 1
                    cycle_start_index = current_path.index(neighbor)
                    cycle_length = len(current_path) - cycle_start_index  # Calculate cycle length based on edges
                    self.min_cycle_length = min(self.min_cycle_length, cycle_length)
        current_path.pop()  # Remove current vertex from the path
        self.rec_stack[v] = False
    def find_cycle(self):
        self.dfs(1, [])  # Start DFS
        return self.min_cycle_length if self.min_cycle_length != float('inf') else None