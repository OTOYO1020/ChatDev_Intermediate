'''
Module to define the Tree class and its methods for calculating distances.
'''
class Tree:
    def __init__(self, n):
        self.n = n
        self.tree = [[] for _ in range(n + 1)]
        self.subtree_size = [0] * (n + 1)
        self.distance_sum = [0] * (n + 1)
    def add_edge(self, a, b):
        self.tree[a].append(b)
        self.tree[b].append(a)
    def dfs_initial(self, v, parent, c):
        self.subtree_size[v] = 1
        for neighbor in self.tree[v]:
            if neighbor != parent:
                # Recursively calculate the distance sum for the child
                self.distance_sum[v] += self.dfs_initial(neighbor, v, c) + c[neighbor - 1]
                self.subtree_size[v] += self.subtree_size[neighbor]
        # No need to add anything for the current vertex as its distance to itself is 0
        return self.distance_sum[v]
    def dfs_recalculate(self, v, parent, c):
        for neighbor in self.tree[v]:
            if neighbor != parent:
                # Adjust the distance sum for the child based on the parent's distance sum
                self.distance_sum[neighbor] = self.distance_sum[v] - self.subtree_size[neighbor] + (self.n - self.subtree_size[neighbor])
                self.dfs_recalculate(neighbor, v, c)
    def calculate_distance_sum(self, root, c):
        # Reset distance_sum to zero before calculations
        self.distance_sum = [0] * (self.n + 1)
        self.dfs_initial(root, -1, c)  # Pass c directly from the context
        self.dfs_recalculate(root, -1, c)
    def find_minimum_distance_sum(self, c):
        # Initialize variables to track the minimum distance sum
        self.calculate_distance_sum(1, c)  # Calculate distance sum for the root first
        min_value = self.distance_sum[1]
        min_vertex = 1
        # Now we can use the recalculated values for the rest of the vertices
        for v in range(2, self.n + 1):
            if self.distance_sum[v] < min_value:
                min_value = self.distance_sum[v]
                min_vertex = v
        return min_value, min_vertex