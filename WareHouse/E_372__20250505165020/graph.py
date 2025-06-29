'''
Module to define the Graph class and its methods for managing edges and queries.
'''
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_list = {i: [] for i in range(1, num_vertices + 1)}
        self.sorted_cache = {}  # Cache for sorted connected vertices
    def add_edge(self, u, v):
        # Check for valid range before proceeding
        if not (1 <= u <= self.num_vertices) or not (1 <= v <= self.num_vertices):
            print(f"Invalid edge: ({u}, {v}) - vertices must be in range 1 to {self.num_vertices}.")
            return False  # Return False for invalid edge
        if u == v:
            print(f"Self-loops are not allowed: {u} cannot connect to itself.")
            return False  # Return False for self-loop
        # Add edge in both directions for undirected graph
        if v not in self.adjacency_list[u]:  # Check for duplicate edge
            self.adjacency_list[u].append(v)
        if u not in self.adjacency_list[v]:  # Check for duplicate edge
            self.adjacency_list[v].append(u)
        # Invalidate cache for both vertices
        self.sorted_cache.pop(u, None)
        self.sorted_cache.pop(v, None)
        return True  # Return True for successful edge addition
    def find_kth_largest(self, v, k):
        if v < 1 or v > self.num_vertices:  # Check if v is within valid range
            return -1  # Invalid vertex
        if k < 1:  # Check if k is valid
            return -1  # Invalid k
        # Check if we have a cached sorted list
        if v not in self.sorted_cache:
            connected_vertices = sorted(self.adjacency_list[v], reverse=True)
            self.sorted_cache[v] = connected_vertices  # Cache the sorted list
        else:
            connected_vertices = self.sorted_cache[v]  # Use cached list
        if len(connected_vertices) >= k:
            return connected_vertices[k - 1]
        return -1