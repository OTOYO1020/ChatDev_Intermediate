'''
Logic file containing the function to find the minimum excluded integer.
'''
from typing import List
def find_minimum_excluded_integer(N: int, M: int, A: List[int]) -> int:
    if len(A) != N:
        raise ValueError("The length of A must be equal to N.")
    # Check for negative integers in A
    if any(a < 0 for a in A):
        raise ValueError("All elements in A must be non-negative integers.")
    # Initialize a set with the original values of A for efficient lookup
    excluded_set = set(A)
    # Perform the update M times
    for m in range(1, M + 1):
        for i in range(N):
            A[i] += (i + 1)  # Update A[i] by adding the current index (1-based)
            excluded_set.add(A[i])  # Add updated value to the set
    # Find the minimum excluded integer
    i = 0
    while i in excluded_set:
        i += 1
    return i