'''
Utility functions for input validation and data processing.
'''
from collections import defaultdict
from typing import List
def validate_input(N, A, C):
    '''
    Validates the input values to ensure they meet the specified constraints.
    '''
    if not (1 <= N <= 200000):
        return False
    if len(A) != N or len(C) != N:
        return False
    if any(not (1 <= a <= 1000000000) for a in A):
        return False
    if any(not (1 <= c <= 1000000000) for c in C):
        return False
    return True
def maximize_min_deliciousness(N: int, A: List[int], C: List[int]) -> int:
    '''
    Groups deliciousness values by color and computes the maximum minimum deliciousness.
    '''
    color_map = defaultdict(list)
    # Group deliciousness values by color
    for i in range(N):
        color_map[C[i]].append(A[i])
    max_min_deliciousness = float('-inf')
    # Find the minimum deliciousness for each color
    for deliciousness_values in color_map.values():
        if deliciousness_values:  # Check if the list is not empty
            min_deliciousness = min(deliciousness_values)
            max_min_deliciousness = max(max_min_deliciousness, min_deliciousness)
    # Handle the case where no valid minimum was found
    if max_min_deliciousness == float('-inf'):
        raise ValueError("No valid minimum deliciousness found. Please check the input data.")
    return max_min_deliciousness