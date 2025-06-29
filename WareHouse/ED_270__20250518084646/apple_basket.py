'''
Module containing the function to calculate remaining apples in baskets.
'''
from typing import List
def remaining_apples(N: int, A: List[int], K: int) -> List[int]:
    '''
    Calculates the remaining apples in each basket after eating K apples.
    Parameters:
    N (int): Number of baskets.
    A (List[int]): List of integers representing apples in each basket.
    K (int): Number of apples to eat.
    Returns:
    List[int]: List of remaining apples in each basket.
    '''
    # Create a copy of A to avoid modifying the original list
    remaining_apples_list = A.copy()
    # Calculate the total number of apples available
    total_apples = sum(remaining_apples_list)
    # Adjust K if it exceeds the total number of apples
    K = min(K, total_apples)
    # If K is zero or if there are no apples, return the original list
    if K == 0 or total_apples == 0:
        return remaining_apples_list
    eaten = 0
    i = 0
    while eaten < K:
        if remaining_apples_list[i] > 0:
            remaining_apples_list[i] -= 1
            eaten += 1
        i = (i + 1) % N  # Wrap around to the start of the list
    return remaining_apples_list