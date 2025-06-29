'''
Main application file for the Minimum Vertices in Tree application.
'''
from typing import List, Tuple
from tree import Tree
def parse_input(N: int, K: int, edges: List[Tuple[int, int]], specified_vertices: List[int]):
    # Validate input
    if len(edges) != N - 1:
        raise ValueError("The number of edges must be N-1 for a tree.")
    if len(specified_vertices) != K:
        raise ValueError("The number of specified vertices must be K.")
    return N, K, edges, specified_vertices
def main(N: int, K: int, edges: List[Tuple[int, int]], specified_vertices: List[int]):
    N, K, edges, specified_vertices = parse_input(N, K, edges, specified_vertices)
    tree = Tree(N, edges)
    result = tree.min_vertices_in_tree(K, specified_vertices)
    print(f"Minimum Vertices: {result}")
if __name__ == "__main__":
    # Example input for testing
    N = 5
    K = 3
    edges = [(1, 2), (1, 3), (2, 4), (2, 5)]
    specified_vertices = [4, 5, 3]
    main(N, K, edges, specified_vertices)