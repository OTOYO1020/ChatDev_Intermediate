'''
Module for counting immediate subordinates based on boss relationships.
'''
from typing import List
def count_subordinates(N: int, A: List[int]) -> List[int]:
    '''
    Count the number of immediate subordinates for each member.
    Parameters:
    N (int): The number of members.
    A (List[int]): The list of immediate bosses for members 2 to N.
    Returns:
    List[int]: A list containing the count of immediate subordinates for each member.
    '''
    subordinate_count = [0] * (N + 1)
    # Validate input values in A
    for i in range(len(A)):
        if A[i] < 1 or A[i] > i + 1:  # Correct condition
            raise ValueError(f"Invalid boss ID {A[i]} at position {i+1} in A. Must be in range [1, {i + 1}].")
    for i in range(2, N + 1):  # Iterate from 2 to N (inclusive)
        subordinate_count[A[i - 2]] += 1  # Increment the count for the boss
    return subordinate_count[1:]  # Exclude index 0