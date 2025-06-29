'''
Graph class to represent the graph and perform DFS.
'''
class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, a, b):
        if a not in self.graph:
            self.graph[a] = []
        if b not in self.graph:
            self.graph[b] = []
        self.graph[a].append(b)
        self.graph[b].append(a)
    def dfs(self, node, parent, required_vertices):
        count = 0
        found_required = node in required_vertices
        if found_required:  # Count the node if it's a required vertex
            count += 1
        found_vertices = {node}  # Initialize with the current node
        for neighbor in self.graph.get(node, []):
            if neighbor != parent:
                child_count, child_found_vertices = self.dfs(neighbor, node, required_vertices)
                count += child_count  # Accumulate the count from child nodes
                found_vertices.update(child_found_vertices)  # Update found vertices
        return count, found_vertices  # Return total count and found vertices