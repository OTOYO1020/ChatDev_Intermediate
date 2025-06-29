'''
Main application class for calculating minimum connected components.
'''
from edge_subset import EdgeSubset
from itertools import combinations
class App:
    def __init__(self):
        self.N = 0
        self.edges = []
    def parse_input(self, input_data):
        lines = input_data.strip().split('\n')
        self.N = int(lines[0])  # First line for N
        self.edges = [tuple(map(int, line.split())) for line in lines[1:]]  # Subsequent lines for edges
    def calculate_min_connected_components(self):
        try:
            if self.N == 0:  # Handle case with no vertices
                return 0
            if not self.edges:  # Handle case with no edges
                return self.N  # Each vertex is its own component
            min_components = float('inf')
            for r in range(len(self.edges) + 1):
                for subset in combinations(self.edges, r):
                    edge_subset = EdgeSubset(subset, self.N)
                    if edge_subset.is_valid(Graph(self.N)):
                        components = edge_subset.count_connected_components()
                        min_components = min(min_components, components)
            return min_components
        except ValueError as ve:
            print(f"Input Error: {str(ve)}")
        except Exception as e:
            print(f"Error: {str(e)}")
    def run(self):
        input_data = input("Enter the number of vertices followed by edges (e.g., '5\n0 1\n1 2\n3 4'): ")
        self.parse_input(input_data)
        result = self.calculate_min_connected_components()
        print(f"Minimum Connected Components: {result}")