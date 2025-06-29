'''
Module for calculating the minimum time required to clear stages.
'''
from typing import List
def calculate_minimum_time(N: int, A: List[int], B: List[int], X: int) -> int:
    '''
    Calculate the minimum time required to clear stages X times.
    Parameters:
    N (int): The number of stages.
    A (List[int]): The list of first clear times for each stage.
    B (List[int]): The list of subsequent clear times for each stage.
    X (int): The number of clears needed for each stage.
    Returns:
    int: The total time required to clear the stages X times.
    '''
    total_time = 0
    for i in range(N):
        # For the first clear of each stage
        if i == 0:
            total_time += A[i] + B[i]  # First clear time for the first stage
        else:
            total_time += B[i]  # First clear time for subsequent stages
        # Calculate additional clears needed for each stage
        if X > 1:  # Only add additional clears if more than one clear is needed
            total_time += (X - 1) * B[i]  # Additional clears after the first
    return total_time