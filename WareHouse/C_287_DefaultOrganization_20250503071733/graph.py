'''
Graph class to represent an undirected graph using an adjacency list.
'''
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {i: [] for i in range(1, vertices + 1)}
    def add_edge(self, u, v):
        # Validate vertices
        if u < 1 or u > self.vertices or v < 1 or v > self.vertices:
            raise ValueError(f"Invalid vertices: {u}, {v}. Vertices must be between 1 and {self.vertices}.")
        if v not in self.adjacency_list[u]:  # Prevent duplicate edges
            self.adjacency_list[u].append(v)
            self.adjacency_list[v].append(u)
    def is_path_graph(self):
        # Check if the number of edges is equal to N - 1
        edge_count = sum(len(neighbors) for neighbors in self.adjacency_list.values()) // 2
        if edge_count != self.vertices - 1:
            return False  # Early return if edge count is not valid
        visited = set()
        self.dfs(1, visited)
        if len(visited) != self.vertices:
            return False
        for neighbors in self.adjacency_list.values():
            if len(neighbors) > 2:
                return False
        return True
    def dfs(self, vertex, visited):
        visited.add(vertex)
        for neighbor in self.adjacency_list[vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)