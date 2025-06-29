'''
Module for calculating the count of subsets with integer averages.
'''
from typing import List
def count_integer_averages(N: int, A: List[int]) -> int:
    '''
    Counts the number of non-empty subsets of A that have an integer average.
    Parameters:
    N (int): Length of the sequence.
    A (List[int]): List of positive integers.
    Returns:
    int: Count of subsets with integer averages, modulo 998244353.
    '''
    MOD = 998244353
    count = 0
    # Validate that all elements in A are positive integers
    if any(a <= 0 for a in A):
        raise ValueError("All elements in the list must be positive integers.")
    # Iterate through all possible non-empty subsets using bit manipulation
    for i in range(1, 1 << N):
        subset_sum = 0
        subset_count = 0
        for j in range(N):
            if i & (1 << j):
                subset_sum += A[j]
                subset_count += 1
        # Check if the average is an integer
        if subset_count > 0 and subset_sum % subset_count == 0:
            count += 1
    return count % MOD