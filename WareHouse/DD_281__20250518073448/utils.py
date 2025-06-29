'''
Utility functions for the Greatest Multiple Application.
'''
from itertools import combinations
def greatest_multiple_of_D(A: list, K: int, D: int) -> int:
    '''
    Calculate the greatest multiple of D from sums of K distinct integers in A.
    Parameters:
    A (list): List of integers.
    K (int): Number of distinct integers to sum.
    D (int): The divisor to find multiples of.
    Returns:
    int: The greatest multiple of D or -1 if none exists.
    '''
    # Generate all possible sums of K distinct integers from A
    S = set(sum(comb) for comb in combinations(A, K))
    # Filter sums to find multiples of D
    multiples_of_D = [s for s in S if s % D == 0]
    # Return the maximum multiple of D found, or -1 if none exist
    return max(multiples_of_D) if multiples_of_D else -1