'''
Module to define the GemGraph class for managing gem adjacency.
'''
class GemGraph:
    def __init__(self):
        self.adjacency_list = {}
    def add_edge(self, a, b):
        if a not in self.adjacency_list:
            self.adjacency_list[a] = []
        if b not in self.adjacency_list:
            self.adjacency_list[b] = []
        self.adjacency_list[a].append(b)
        self.adjacency_list[b].append(a)
    def get_connected_components(self):
        visited = set()
        components = []
        def dfs(node, component):
            visited.add(node)
            component.append(node)
            for neighbor in self.adjacency_list.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor, component)
        for gem in self.adjacency_list:
            if gem not in visited:
                component = []
                dfs(gem, component)
                components.append(component)
        return components