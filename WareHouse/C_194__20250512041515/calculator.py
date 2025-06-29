'''
Module for calculating the sum of squared differences.
'''
from typing import List
def sum_of_squared_differences(N: int, A: List[int]) -> int:
    '''
    Calculate the sum of squared differences for the given list A.
    Parameters:
    N (int): The number of elements in the list A.
    A (List[int]): The list of integers.
    Returns:
    int: The sum of squared differences.
    '''
    total_sum = 0
    # Iterate over all pairs (i, j) where 1 ≤ j < i ≤ N
    for i in range(N):
        for j in range(i):
            total_sum += (A[i] - A[j]) ** 2
    return total_sum