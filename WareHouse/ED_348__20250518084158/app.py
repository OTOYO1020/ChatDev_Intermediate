'''
Application class to manage the tree distance application.
'''
from tree import Tree
from input_handler import InputHandler
class App:
    def __init__(self):
        self.tree = None
    def run(self):
        input_data = input("Enter the input data:\n")
        handler = InputHandler(input_data)
        try:
            n, edges, C = handler.parse_input()
        except ValueError as e:
            print(f"Input error: {e}")
            return
        self.tree = Tree(n)
        self.tree.C = C
        for a, b in edges:
            self.tree.add_edge(a, b)
        self.tree.dfs(1, -1)  # Initialize depths and subtree sizes
        # Calculate f(v) for all vertices from 1 to N efficiently
        f_values = self.tree.calculate_f_values()
        # Find the minimum value and corresponding vertex
        min_value = min(f_values[1:])  # Ignore index 0
        min_vertex = f_values[1:].index(min_value) + 1  # Adjust index to match vertex numbering
        print(f"Minimum f(v): {min_value} at vertex: {min_vertex}")