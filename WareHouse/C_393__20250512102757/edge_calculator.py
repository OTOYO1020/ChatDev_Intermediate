'''
Contains the logic for calculating the minimum number of edges to remove from a graph.
'''
from typing import List, Tuple
def min_edges_to_remove(N: int, M: int, edges: List[Tuple[int, int]]) -> int:
    '''
    Calculate the minimum number of edges to remove to eliminate self-loops and multi-edges.
    Parameters:
    N (int): Number of vertices.
    M (int): Number of edges.
    edges (List[Tuple[int, int]]): List of edges represented as tuples.
    Returns:
    int: Minimum number of edges to remove.
    '''
    unique_edges = {}
    self_loops = 0
    for u, v in edges:
        if u == v:
            self_loops += 1
        else:
            edge = (min(u, v), max(u, v))  # Store edges in a consistent order
            if edge in unique_edges:
                unique_edges[edge] += 1
            else:
                unique_edges[edge] = 1
    # The number of multi-edges is the sum of (count - 1) for each edge that appears more than once
    multi_edges = sum(count - 1 for count in unique_edges.values() if count > 1)
    # Return the total count of edges to remove
    return self_loops + multi_edges