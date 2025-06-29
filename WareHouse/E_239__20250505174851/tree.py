'''
Module to define the TreeNode and Tree classes for managing the tree structure.
'''
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
    def add_child(self, child_node):
        self.children.append(child_node)
class Tree:
    def __init__(self):
        self.nodes = {}
        self.root = None
        self.values = {}  # Store values for each vertex
    def add_edge(self, parent_value, child_value):
        if parent_value not in self.nodes:
            self.nodes[parent_value] = TreeNode(parent_value)
        if child_value not in self.nodes:
            self.nodes[child_value] = TreeNode(child_value)
        # Set the root only if it hasn't been set yet
        if self.root is None:
            self.root = self.nodes[parent_value]
        self.nodes[parent_value].add_child(self.nodes[child_value])
    def set_value(self, vertex, value):
        if vertex < 1:  # Ensure vertex is 1-indexed
            raise ValueError("Vertex index must be 1 or greater.")
        self.values[vertex] = value
    def dfs(self, node):
        if node is None:  # Handle case where node is None
            return []
        values = [self.values[node.value]]  # Use the stored values
        for child in node.children:
            values.extend(self.dfs(child))
        return values
    def find_kth_largest(self, v, k):
        if v not in self.nodes:
            raise ValueError("Invalid vertex.")
        subtree_values = self.dfs(self.nodes[v])
        subtree_values.sort(reverse=True)
        if k <= len(subtree_values):
            return subtree_values[k - 1]
        else:
            return None  # Return None instead of raising an error