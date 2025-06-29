'''
Module to perform depth-first search on the graph and calculate scores.
'''
class DFS:
    def __init__(self, graph, values):
        self.graph = graph
        self.values = values
        self.max_score = 0
    def dfs(self, vertex, visited, path):
        if vertex in visited:
            return
        visited.add(vertex)
        # Append current vertex's value to the path
        path.append(self.values[vertex - 1])
        # Check if the current path is non-decreasing
        if len(path) > 1 and self.values[vertex - 1] < path[-2]:
            visited.remove(vertex)
            path.pop()
            return
        # If we reached the last vertex (N), calculate distinct integers
        if vertex == len(self.values):  # Check against the number of vertices
            distinct_count = len(set(path))
            self.max_score = max(self.max_score, distinct_count)
        # Explore neighbors
        for neighbor in self.graph.graph[vertex]:
            self.dfs(neighbor, visited, path)  # Use the same path to avoid unnecessary copying
        visited.remove(vertex)
        path.pop()
    def find_max_score(self):
        visited = set()
        self.dfs(1, visited, [])
        return self.max_score