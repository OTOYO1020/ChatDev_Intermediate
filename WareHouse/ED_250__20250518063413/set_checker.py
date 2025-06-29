'''
Module to check equality of sets derived from two sequences based on queries.
'''
from typing import List, Tuple
def check_equal_sets(A: List[int], B: List[int], queries: List[Tuple[int, int]]) -> List[str]:
    results = []
    for x_i, y_i in queries:
        # Ensure x_i and y_i are non-negative
        if x_i < 0 or y_i < 0:
            results.append('No')  # Invalid query
            continue
        # Adjust x_i and y_i to the lengths of A and B respectively
        x_i = min(x_i, len(A))
        y_i = min(y_i, len(B))
        # Extract the first x_i terms from A and y_i terms from B
        set_a = set(A[:x_i])
        set_b = set(B[:y_i])
        # Compare the two sets and append the result
        if set_a == set_b:
            results.append('Yes')
        else:
            results.append('No')
    return results