'''
Tree class to manage the tree structure and counters.
'''
class Tree:
    def __init__(self, n):
        self.n = n
        self.counters = [0] * (n + 1)  # 1-indexed array for counters
        self.adjacency_list = [[] for _ in range(n + 1)]  # Adjacency list for the tree
        self.increment = [0] * (n + 1)  # To store increments for each node
    def add_edge(self, a, b):
        # Add an edge between vertices a and b in the adjacency list
        self.adjacency_list[a].append(b)
        self.adjacency_list[b].append(a)
    def update_counters(self, p, x):
        # Store the increment for the node p
        self.increment[p] += x  
    def dfs(self, node, parent, current_increment):
        # Apply the increment to the current node
        current_increment += self.increment[node]  # Carry forward the increment from the parent
        self.counters[node] += current_increment  # Update the counter with the current increment
        for neighbor in self.adjacency_list[node]:
            if neighbor != parent:  # Avoid going back to the parent
                self.dfs(neighbor, node, current_increment)  # Pass the current increment to children
        # Reset the increment after processing to avoid affecting other nodes
        self.increment[node] = 0
    def finalize_counters(self, root=1):
        # Start DFS from the specified root with initial increment of 0
        self.dfs(root, -1, 0)
    def get_counters(self):
        # Return the counters excluding the 0th index
        return self.counters[1:]  