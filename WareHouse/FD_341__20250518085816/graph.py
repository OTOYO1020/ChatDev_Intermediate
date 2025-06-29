'''
Graph class to represent the graph structure and perform operations.
'''
from typing import List, Tuple
class Graph:
    def __init__(self, N: int, M: int, edges: List[Tuple[int, int]], weights: List[int], pieces: List[int]):
        self.N = N
        self.M = M
        self.edges = edges
        self.weights = weights
        self.pieces = pieces
        self.adjacency_list = self.build_adjacency_list()
    def build_adjacency_list(self):
        adj_list = {i: [] for i in range(self.N)}
        for u, v in self.edges:
            # Adjust for 0-indexing
            adj_list[u].append(v)
            adj_list[v].append(u)
        return adj_list
    def calculate_max_placeable(self, vertex: int) -> int:
        # Calculate how many more pieces can be placed on vertex based on weights
        return self.weights[vertex] - self.pieces[vertex]
    def max_operations(self):
        total_operations = 0
        while True:
            any_operation = False
            for x in range(self.N):
                if self.pieces[x] > 0:
                    adjacent_vertices = self.adjacency_list[x]
                    # Filter adjacent vertices based on the weight condition
                    valid_vertices = [v for v in adjacent_vertices if self.weights[v] < self.weights[x]]
                    sum_weights = sum(self.weights[v] for v in valid_vertices)
                    # Ensure the sum of weights of valid vertices is strictly less than the weight of vertex x
                    if sum_weights < self.weights[x] and valid_vertices:
                        for v in valid_vertices:
                            # Allow multiple placements until no more pieces can be placed
                            while self.pieces[x] > 0:
                                max_placeable = self.calculate_max_placeable(v)
                                pieces_to_place = min(self.pieces[x], max_placeable)
                                if pieces_to_place > 0:
                                    self.pieces[x] -= pieces_to_place
                                    self.pieces[v] += pieces_to_place
                                    total_operations += pieces_to_place
                                    any_operation = True
                                else:
                                    break  # Break if no more pieces can be placed on vertex v
                if self.pieces[x] <= 0:  # Break if no pieces left at vertex x
                    break
            if not any_operation:
                break
        return total_operations