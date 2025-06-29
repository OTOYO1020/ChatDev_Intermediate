'''
Module for calculating maximum happiness points based on children's activeness values.
This module contains the function to compute the maximum happiness points
by evaluating all permutations of children's activeness values.
'''
from itertools import permutations
from typing import List
def max_happiness(N: int, A: List[int]) -> int:
    '''
    Calculate the maximum total happiness points based on the activeness values.
    Parameters:
    N (int): Number of children.
    A (List[int]): List of activeness values for the children.
    Returns:
    int: Maximum happiness points.
    '''
    max_hap = 0
    # Generate all permutations of the list A
    for perm in permutations(A):
        total_happiness = 0
        # Calculate happiness for the current permutation
        for x in range(N):
            total_happiness += perm[x] * abs(x - perm.index(perm[x]))  # Corrected logic
        max_hap = max(max_hap, total_happiness)
    return max_hap