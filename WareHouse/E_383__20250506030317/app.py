'''
Main application class for the command line interface.
'''
from graph import Graph
from permutation_calculator import PermutationCalculator
class App:
    def __init__(self, input_data):
        self.input_data = input_data
    def run(self):
        try:
            # Read number of vertices and edges
            first_line = self.input_data[0].strip().split()
            vertices = int(first_line[0])
            edges_count = int(first_line[1])
            graph = Graph(vertices)
            # Check if we have enough lines for edges
            if len(self.input_data) < edges_count + 1:
                raise ValueError(f"Expected {edges_count} edges, but got {len(self.input_data) - 1}.")
            # Read edges
            for i in range(1, edges_count + 1):
                edge = self.input_data[i].strip()
                parts = list(map(int, edge.split()))
                if len(parts) != 3:
                    raise ValueError(f"Each edge must be in the format 'u v w'. Found: {edge}")
                u, v, w = parts
                if u < 1 or u > vertices or v < 1 or v > vertices:
                    raise ValueError(f"Vertices {u} and {v} must be within the range 1 to {vertices}.")
                graph.add_edge(u, v, w)
            # Check if we have enough lines for K and sequences A and B
            if len(self.input_data) < edges_count + 4:
                raise ValueError("Not enough lines provided for K and sequences A and B.")
            # Read K and sequences A and B
            K = int(self.input_data[edges_count + 1].strip())
            A = list(map(int, self.input_data[edges_count + 2].strip().split()))
            B = list(map(int, self.input_data[edges_count + 3].strip().split()))
            if len(A) != K or len(B) != K:
                raise ValueError("Sequences A and B must be of length K.")
            # Validate that all vertices in A and B are within the valid range (1-based indexing)
            for vertex in A + B:
                if vertex < 1 or vertex > vertices:
                    raise ValueError(f"Vertex {vertex} is out of bounds. Valid range is 1 to {vertices}.")
            # Calculate minimum sum
            min_sum = PermutationCalculator.calculate_min_sum(A, B, graph)
            if min_sum is None or min_sum == float('inf'):
                print("No valid path exists for the given sequences.")
            else:
                print(f"Minimum sum: {min_sum}")
        except Exception as e:
            print(f"Error: {str(e)}")