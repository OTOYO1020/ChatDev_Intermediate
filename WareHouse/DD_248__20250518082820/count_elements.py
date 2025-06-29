'''
Module for counting occurrences of integers in a list based on queries.
'''
from typing import List, Tuple
def count_elements(A: List[int], queries: List[Tuple[int, int, int]]) -> List[int]:
    results = []
    for L, R, X in queries:
        # Adjust for 0-based indexing
        subarray = A[L-1:R]
        count = subarray.count(X)  # Count occurrences of X in the subarray
        results.append(count)  # Store the count in results
    return results