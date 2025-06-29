'''
Graph class to represent an undirected graph and perform BFS.
'''
from collections import deque
class Graph:
    def __init__(self, N):
        self.N = N
        self.adjacency_list = [[] for _ in range(N + 1)]  # Change to list of lists for order
    def add_edge(self, a, b):
        '''
        Add an undirected edge between vertices a and b.
        Parameters:
            a (int): The first vertex.
            b (int): The second vertex.
        '''
        if b not in self.adjacency_list[a]:  # Check for duplicates
            self.adjacency_list[a].append(b)
        if a not in self.adjacency_list[b]:  # Check for duplicates
            self.adjacency_list[b].append(a)
    def bfs(self, start, stamina):
        '''
        Perform BFS starting from the vertex 'start' and return all reachable vertices
        within 'stamina' edges.
        '''
        if start < 1 or start > self.N:  # Check for valid starting vertex
            return set()  # Return empty set if start is out of bounds
        if stamina < 0:  # Check for negative stamina
            return set()
        guarded_vertices = set()
        if not self.adjacency_list[start]:  # Check if there are no edges from the start vertex
            return guarded_vertices  # Return empty set if no edges
        guarded_vertices.add(start)  # Always add the starting vertex
        if stamina == 0:  # If stamina is zero, return only the starting vertex
            return guarded_vertices
        visited = [False] * (self.N + 1)
        queue = deque([(start, 0)])
        visited[start] = True
        while queue:
            current, depth = queue.popleft()
            if depth < stamina:
                for neighbor in self.adjacency_list[current]:  # No need to sort here
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append((neighbor, depth + 1))
                        guarded_vertices.add(neighbor)  # Add neighbors to guarded vertices
        return guarded_vertices  # Return the set of guarded vertices