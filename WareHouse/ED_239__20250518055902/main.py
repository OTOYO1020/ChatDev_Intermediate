'''
Main entry point for the application.
'''
from tree import Tree
from typing import List, Tuple
def find_kth_largest_in_subtree(N: int, edges: List[Tuple[int, int]], values: List[int], queries: List[Tuple[int, int]]) -> List[int]:
    tree = Tree(N, edges, values)
    results = [tree.find_kth_largest_in_subtree(v, k) for v, k in queries]
    return results
if __name__ == "__main__":
    # Example usage
    N = 5
    edges = [(0, 1), (0, 2), (1, 3), (1, 4)]
    values = [5, 3, 8, 6, 2]
    queries = [(0, 2), (1, 1), (3, 1)]
    print(find_kth_largest_in_subtree(N, edges, values, queries))