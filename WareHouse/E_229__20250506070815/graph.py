'''
Graph class to represent an undirected graph and perform operations on it.
'''
class Graph:
    def __init__(self, n):
        self.n = n
        self.adjacency_list = {i: [] for i in range(1, n + 1)}
    def add_edge(self, a, b):
        self.adjacency_list[a].append(b)
        self.adjacency_list[b].append(a)
    def delete_vertex(self, vertex):
        if vertex in self.adjacency_list:
            # Remove the vertex from its neighbors' adjacency lists
            for neighbor in self.adjacency_list[vertex]:
                self.adjacency_list[neighbor].remove(vertex)
            # Remove the vertex from the adjacency list
            del self.adjacency_list[vertex]
    def count_connected_components(self, deleted):
        visited = set()
        count = 0
        def dfs(v):
            visited.add(v)
            for neighbor in self.adjacency_list[v]:
                if neighbor not in visited and neighbor not in deleted:
                    dfs(neighbor)
        for vertex in self.adjacency_list:
            if vertex not in visited and vertex not in deleted:
                dfs(vertex)
                count += 1
        return count