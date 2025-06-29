'''
Graph and GraphOperations classes for handling graph structure and operations.
'''
import random
from fractions import Fraction
class Graph:
    def __init__(self, N, edges):
        '''
        Initializes the graph with N vertices and the given edges.
        Parameters:
        N (int): Number of vertices.
        edges (list of tuples): List of edges connecting the vertices.
        '''
        self.N = N
        self.edges = list(set(edges))  # Store unique edges
    def get_random_edge(self):
        '''
        Returns a random edge from the graph.
        Returns:
        tuple: A randomly selected edge (x, y).
        '''
        return random.choice(self.edges)
class GraphOperations:
    def __init__(self, graph, A):
        '''
        Initializes the graph operations with a graph and initial values.
        Parameters:
        graph (Graph): The graph object.
        A (list): Initial values for each vertex.
        '''
        self.graph = graph
        self.A = [Fraction(a) for a in A]  # Store initial values as Fractions
    def perform_operations(self, K, M):
        '''
        Simulates K operations on the graph, updating vertex values.
        Parameters:
        K (int): Number of operations to perform.
        M (int): Number of edges to select in each operation.
        Returns:
        list: Final values of the vertices after K operations.
        '''
        update_count = [0] * self.graph.N  # Track how many times each vertex is updated
        for _ in range(K):
            for _ in range(min(M, len(self.graph.edges))):  # Ensure we don't exceed available edges
                x, y = self.graph.get_random_edge()
                mean_value = (self.A[x] + self.A[y]) / 2  # Mean as a Fraction
                self.A[x] = mean_value  # Update vertex x with the mean value
                self.A[y] = mean_value  # Update vertex y with the mean value
                update_count[x] += 1
                update_count[y] += 1
        # Calculate expected values
        expected_values = []
        MOD = 10**9 + 7
        for i in range(self.graph.N):
            if update_count[i] > 0:
                y = self.A[i].numerator  # Final value after updates
                x = update_count[i]  # Number of updates
                z = (y * pow(x, MOD - 2, MOD)) % MOD  # Modular inverse calculation
            else:
                # If the vertex was never updated, its expected value is its initial value
                z = (self.A[i].numerator * pow(1, MOD - 2, MOD)) % MOD  # Use the initial value directly
            expected_values.append(z % MOD)  # Ensure z is within the range [0, 10^9 + 6]
        return expected_values