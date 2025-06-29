'''
EdgeSubset class to handle subsets of edges and check their validity.
'''
from graph import Graph
class EdgeSubset:
    def __init__(self, edges, N):
        self.edges = edges
        self.N = N
    def is_valid(self, graph):
        visited = [False] * self.N
        def dfs(v):
            visited[v] = True
            for neighbor in graph.adj_list[v]:
                if not visited[neighbor]:
                    dfs(neighbor)
        for u in range(self.N):
            if not visited[u]:
                dfs(u)
                # After DFS, collect all vertices in the component
                component_vertices = [i for i in range(self.N) if visited[i]]
                # Check if all pairs of vertices in the component are directly connected
                edges_set = set((min(u, v), max(u, v)) for u in component_vertices for v in graph.adj_list[u] if v in component_vertices)
                for i in range(len(component_vertices)):
                    for j in range(i + 1, len(component_vertices)):
                        if (min(component_vertices[i], component_vertices[j]), max(component_vertices[i], component_vertices[j])) not in edges_set:
                            return False
                # Reset visited for the next component check
                for v in component_vertices:
                    visited[v] = False
        return True
    def count_connected_components(self):
        graph = Graph(self.N)
        for u, v in self.edges:
            graph.add_edge(u, v)
        return graph.connected_components()