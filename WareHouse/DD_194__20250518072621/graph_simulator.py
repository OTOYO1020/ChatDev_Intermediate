'''
Contains the GraphSimulator class that simulates the graph operations.
'''
class GraphSimulator:
    def expected_operations(self, N: int) -> float:
        '''
        Calculate the expected number of operations until the graph becomes connected.
        Parameters:
        N (int): The number of vertices in the graph.
        Returns:
        float: The expected number of operations required to connect all vertices.
        '''
        if N <= 1:
            return 0.0  # No operations needed for 0 or 1 vertex
        operations_count = 0.0
        connected_vertices = 1  # Start with one vertex connected
        while connected_vertices < N:
            # Probability of connecting a new vertex
            probability_of_new_connection = (N - connected_vertices) / N
            expected_trials = 1 / probability_of_new_connection
            operations_count += expected_trials
            connected_vertices += 1  # Increment the count of connected vertices
        return operations_count