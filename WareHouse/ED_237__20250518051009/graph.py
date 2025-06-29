'''
Graph representation for spaces and slopes.
'''
from collections import defaultdict
class Graph:
    def __init__(self, N, H, slopes):
        self.N = N
        self.H = H
        self.slopes = slopes
        self.adjacency_list = defaultdict(list)
        self.build_graph()
    def build_graph(self):
        for u, v in self.slopes:
            self.adjacency_list[u - 1].append(v - 1)
            self.adjacency_list[v - 1].append(u - 1)
    def happiness_change(self, u, v):
        # Calculate the change in happiness when moving from u to v
        change = self.H[v] - self.H[u]
        return max(change, 0)  # Ensure happiness change is not negative
    def max_happiness(self):
        visited = set()  # Use a set to track visited nodes
        # Initialize max_hap to the current happiness (0)
        max_hap = self.dfs(0, visited, 0)
        return max_hap  # Return the maximum happiness found
    def dfs(self, node, visited, current_happiness):
        visited.add(node)  # Mark the node as visited
        max_hap = current_happiness  # Initialize max_hap with the current happiness
        for neighbor in self.adjacency_list[node]:
            if neighbor not in visited:  # Only explore unvisited neighbors
                change = self.happiness_change(node, neighbor)
                new_happiness = current_happiness + change
                max_hap = max(max_hap, self.dfs(neighbor, visited, new_happiness))
        visited.remove(node)  # Backtrack: remove the node from visited
        return max_hap