'''
Contains the function to find recent positions of integers in a list.
'''
from typing import List
def find_recent_positions(N: int, A: List[int]) -> List[int]:
    '''
    Finds the most recent positions of each number in the sequence.
    Parameters:
    N (int): The length of the sequence.
    A (List[int]): The list of positive integers.
    Returns:
    List[int]: A list of integers representing the most recent positions.
    '''
    last_seen = {}
    B = [-1] * N  # Initialize the result list with -1
    for i in range(N):
        if A[i] in last_seen:
            B[i] = last_seen[A[i]]
        last_seen[A[i]] = i  # Update the last seen position
    return B