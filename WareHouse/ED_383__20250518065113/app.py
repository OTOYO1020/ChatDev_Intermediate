'''
Function to calculate the minimum path weight based on given parameters.
'''
from graph import Graph
from itertools import permutations
from typing import List, Tuple
def min_path_weight(N: int, M: int, edges: List[Tuple[int, int, int]], K: int, A: List[int], B: List[int]) -> int:
    if len(A) != K or len(B) != K:
        raise ValueError("The lengths of sequences A and B must equal K.")
    if N <= 0 or M < 0 or K <= 0:
        raise ValueError("N must be positive, M must be non-negative, and K must be positive.")
    # Validate that all vertices in A and B are within the valid range
    for vertex in A + B:
        if vertex < 0 or vertex >= N:
            raise ValueError(f"Vertex {vertex} is out of bounds. Valid range is 0 to {N-1}.")
    # Check for duplicates in sequences A and B
    if len(set(A)) != len(A) or len(set(B)) != len(B):
        raise ValueError("Sequences A and B must not contain duplicate vertices.")
    # If there are no edges and K > 0, return inf immediately
    if M == 0:
        if K > 0:
            return float('inf')  # Return inf instead of raising an error
        else:
            return 0  # If K is 0, no paths to calculate, return 0
    graph = Graph(N)
    for u, v, weight in edges:
        if u < 0 or u >= N or v < 0 or v >= N:
            raise ValueError(f"Edge references invalid vertices: {u}, {v}. Valid range is 0 to {N-1}.")
        graph.add_edge(u, v, weight)
    min_total_weight = float('inf')
    unique_permutations = set(permutations(B))  # Use set to avoid duplicate permutations
    for perm in unique_permutations:
        total_weight = 0
        valid_permutation = True  # Flag to check if the current permutation is valid
        for i in range(K):
            path_weight = graph.f(A[i], perm[i])
            if path_weight == float('inf'):
                valid_permutation = False  # Mark as invalid if any path is infinite
                break
            total_weight += path_weight
        if valid_permutation:
            min_total_weight = min(min_total_weight, total_weight)
    if min_total_weight == float('inf'):
        return float('inf')  # Return inf if no valid paths were found for any permutation
    return min_total_weight  # Return the minimum total path weight found