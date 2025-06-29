'''
Contains the logic for transforming and sorting a permutation.
'''
from typing import List
def transform_permutation(N: int, A: List[int]) -> List[int]:
    '''
    Sorts the given permutation A of size N into the ordered sequence (1, 2, ..., N)
    using a selection sort algorithm with pair swapping.
    '''
    if N <= 0:
        raise ValueError("N must be a positive integer.")
    if len(A) != N or sorted(A) != list(range(1, N + 1)):
        raise ValueError("Invalid permutation input. A must be a permutation of integers from 1 to N.")
    # Implementing a selection sort with pair swapping
    for i in range(N):
        for j in range(i + 1, N):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
            # Check if the list is sorted after the swap
            if A == list(range(1, N + 1)):
                return A  # Return early if sorted
    return A  # Return the sorted list