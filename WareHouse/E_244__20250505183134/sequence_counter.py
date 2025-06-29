'''
Module to define the SequenceCounter class for counting valid sequences.
'''
class SequenceCounter:
    def __init__(self, graph, k, s, t, x):
        self.graph = graph
        self.k = k
        self.s = s
        self.t = t
        self.x = x
        self.memo = {}
    def count_sequences(self, current_vertex, remaining_steps, even_count):
        # Base case: if no remaining steps
        if remaining_steps == 0:
            # Check if we are at the target vertex T and even_count is even
            if current_vertex == self.t and even_count % 2 == 0:
                return 1  # Valid sequence
            else:
                return 0  # Invalid sequence
        # Check memoization to avoid redundant calculations
        if (current_vertex, remaining_steps, even_count) in self.memo:
            return self.memo[(current_vertex, remaining_steps, even_count)]
        # Check if there are neighbors to explore
        if not self.graph.adjacency_list[current_vertex]:
            return 0  # No neighbors to explore, return 0
        total_count = 0
        # Loop through each neighbor of the current vertex
        for neighbor in self.graph.adjacency_list[current_vertex]:
            # If the neighbor is X, increment the even_count
            if neighbor == self.x:
                total_count = (total_count + self.count_sequences(neighbor, remaining_steps - 1, even_count + 1)) % 998244353
            else:
                total_count = (total_count + self.count_sequences(neighbor, remaining_steps - 1, even_count)) % 998244353
        # Store the result in the memoization dictionary
        self.memo[(current_vertex, remaining_steps, even_count)] = total_count
        return total_count