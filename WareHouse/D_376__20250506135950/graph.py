'''
Graph class for representing a directed graph and detecting cycles using DFS.
'''
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(1, vertices + 1)}
    def add_edge(self, a, b):
        '''Add a directed edge from vertex a to vertex b.'''
        self.graph[a].append(b)
    def dfs(self, vertex, visited, rec_stack):
        '''Perform DFS to detect cycles in the graph.'''
        visited.add(vertex)  # Mark the current vertex as visited
        rec_stack.append(vertex)  # Track the current path
        cycle_found = False  # Flag to indicate if a cycle is found
        cycle_length = float('inf')  # Initialize cycle length to infinity
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                # Recur for the neighbor
                result = self.dfs(neighbor, visited, rec_stack)
                if result is not None:
                    cycle_length = min(cycle_length, result)  # Update minimum cycle length
            elif neighbor in rec_stack:  # Cycle detected
                cycle_found = True
                if 1 in rec_stack:  # Check if vertex 1 is in the current path
                    cycle_length = min(cycle_length, len(rec_stack) - rec_stack.index(neighbor))  # Calculate cycle length
        rec_stack.pop()  # Backtrack from the current vertex
        return cycle_length if cycle_found and cycle_length < float('inf') else None  # Return cycle length if found, else None
    def detect_cycle(self):
        '''Detect cycles in the graph starting from vertex 1.'''
        visited = set()  # Set to track visited vertices
        rec_stack = []  # Stack to track the current path
        result = self.dfs(1, visited, rec_stack)  # Start DFS from vertex 1
        if result is not None and result < float('inf'):
            return f"Minimum cycle length containing vertex 1: {result}"
        return "No cycle exists containing vertex 1."