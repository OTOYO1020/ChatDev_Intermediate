'''
Graph class to represent the graph and count connected components.
'''
class Graph:
    def __init__(self, N, edges):
        self.N = N
        self.edges = edges
        self.adj_list = {i: [] for i in range(1, N + 1)}
        for u, v in edges:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
        self.deleted_vertices = set()  # Track deleted vertices
    def count_connected_components(self):
        visited = [False] * (self.N + 1)
        count = 0
        def dfs(vertex):
            stack = [vertex]
            while stack:
                v = stack.pop()
                for neighbor in self.adj_list[v]:
                    if not visited[neighbor] and neighbor not in self.deleted_vertices:
                        visited[neighbor] = True
                        stack.append(neighbor)
        for vertex in range(1, self.N + 1):
            if not visited[vertex] and vertex not in self.deleted_vertices:
                visited[vertex] = True
                dfs(vertex)
                count += 1
        return count
    def delete_vertex(self, vertex):
        # Mark the vertex as deleted
        self.deleted_vertices.add(vertex)
        # Store the edges to restore later
        edges_to_restore = self.adj_list[vertex][:]
        # Remove the vertex from the adjacency list
        for neighbor in edges_to_restore:
            if neighbor in self.adj_list:  # Check if the neighbor exists in the adjacency list
                self.adj_list[neighbor].remove(vertex)  # Remove the edge from neighbor to vertex
        del self.adj_list[vertex]  # Remove the vertex from the adjacency list
        return edges_to_restore  # Return the edges to restore later
    def restore_vertex(self, vertex, edges):
        # Restore the vertex and its edges
        self.deleted_vertices.remove(vertex)
        self.adj_list[vertex] = []  # Initialize the adjacency list for the restored vertex
        for neighbor in edges:
            if neighbor in self.adj_list:  # Ensure the neighbor still exists
                self.adj_list[neighbor].append(vertex)  # Restore the edge from neighbor to vertex
                self.adj_list[vertex].append(neighbor)  # Restore the edge from vertex to neighbor