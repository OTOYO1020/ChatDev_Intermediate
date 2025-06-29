'''
Application for the graph simulation.
'''
from graph import Graph, GraphOperations
class App:
    def __init__(self, input_data):
        '''
        Initializes the application with input data.
        Parameters:
        input_data (list): List of input strings containing N, M, K, edges, and initial values.
        '''
        self.input_data = input_data
        self.master = None  # GUI not implemented; using console input instead
    def run_simulation(self):
        '''
        Runs the graph simulation based on the input data.
        '''
        # Parse input data
        N, M, K = map(int, self.input_data[0].split(','))
        edges = [tuple(map(int, edge.split())) for edge in self.input_data[1:N]]  # Read edges
        edges = [(x - 1, y - 1) for x, y in edges]  # Adjust for 0-based indexing
        A = list(map(int, self.input_data[N].split()))  # Read initial values
        graph = Graph(N, edges)
        operations = GraphOperations(graph, A)
        final_values = operations.perform_operations(K, M)
        # Output final values
        print(f"Final Values: {final_values}")