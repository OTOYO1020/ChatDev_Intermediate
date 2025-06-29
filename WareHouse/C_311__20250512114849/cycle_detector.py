'''
Module for detecting directed cycles in a graph.
'''
class CycleDetector:
    '''
    Class to detect cycles in a directed graph.
    '''
    def __init__(self, N, A):
        '''
        Initializes the class with the number of vertices and the list of edges.
        '''
        self.N = N
        self.adjacency_list = self.build_adjacency_list(A)
        self.visited = [False] * (N + 1)
    def build_adjacency_list(self, edges):
        '''
        Builds an adjacency list from the list of edges.
        Validates that edges are within the correct range.
        Allows self-loops and multiple edges.
        '''
        adjacency_list = {i: [] for i in range(1, self.N + 1)}
        for i in range(0, len(edges), 2):
            u = edges[i]
            v = edges[i + 1]
            if u < 1 or u > self.N or v < 1 or v > self.N:
                raise ValueError(f"Edge vertices must be between 1 and {self.N}.")
            adjacency_list[u].append(v)  # Allow multiple edges
        return adjacency_list
    def find_directed_cycle(self):
        '''
        Main method to find and return the directed cycle.
        '''
        for vertex in range(1, self.N + 1):
            if not self.visited[vertex]:
                path = []  # Reset path for each new starting vertex
                current_path = set()  # Reset current path for each new starting vertex
                cycle = self.dfs(vertex, path, current_path)
                if cycle:
                    return cycle
        return []
    def dfs(self, vertex, path, current_path):
        '''
        Helper method for depth-first search to detect cycles.
        '''
        if vertex in current_path:
            # Cycle detected, construct the cycle path
            cycle_start_index = path.index(vertex)
            cycle_path = path[cycle_start_index:] + [vertex]
            if len(cycle_path) >= 2:  # Ensure at least 2 vertices in the cycle
                return cycle_path
            return None  # Cycle is not valid if it has less than 2 vertices
        # Mark the vertex as part of the current path
        current_path.add(vertex)
        path.append(vertex)  # Use append to maintain order
        # Follow the directed edges
        for next_vertex in self.adjacency_list[vertex]:
            if next_vertex not in current_path:  # Only visit unvisited vertices in the current path
                cycle = self.dfs(next_vertex, path, current_path)
                if cycle:
                    return cycle
        path.pop()  # Use pop to remove the last vertex
        current_path.remove(vertex)  # Remove from current path
        self.visited[vertex] = True  # Mark as visited after exploring all neighbors
        return None