'''
Module to create the application for MST Queries.
'''
from graph import Graph
from typing import List, Tuple
def minimum_spanning_tree_queries(N: int, M: int, edges: List[Tuple[int, int, int]], Q: int, queries: List[Tuple[int, int, int]]) -> List[str]:
    '''
    Handles the input parameters and processes the MST queries.
    '''
    graph = Graph(N)
    for u, v, w in edges:
        graph.add_edge(u, v, w)
    # Compute the original MST
    original_mst = graph.kruskal_mst()
    mst_edges_set = {(min(u, v), max(u, v), w) for w, u, v in original_mst}
    results = []
    for u, v, w in queries:
        # Create a temporary union-find structure to check if adding this edge would create a cycle
        parent = list(range(N))
        rank = [0] * N
        # Add original edges to union-find
        for weight, start, end in graph.edges:
            graph.union(parent, rank, start, end)
        # Now add the new edge to the union-find structure
        if graph.find_parent(parent, u) == graph.find_parent(parent, v):
            results.append("No")  # It creates a cycle
        else:
            results.append("Yes")  # It does not create a cycle
            graph.union(parent, rank, u, v)  # Optionally union the new edge
    return results