'''
Module containing the logic to calculate the minimum number of colors required.
'''
from typing import List
def min_colors_required(N: int, A: List[int]) -> int:
    '''
    Calculate the minimum number of colors required for the given list of integers.
    Parameters:
    N (int): The number of integers in the list.
    A (List[int]): The list of integers.
    Returns:
    int: The minimum number of colors required.
    '''
    if len(A) != N:
        raise ValueError(f"Expected {N} integers, but got {len(A)} integers in the list A.")
    A.sort()  # Sort the list to facilitate color assignment
    color_count = 0  # Initialize color count
    last_color = None  # Variable to track the last assigned color
    for number in A:
        if number != last_color:  # Only increment color count for new unique integers
            color_count += 1  # Increment color count for a new unique integer
            last_color = number  # Update the last color to the current number
    return color_count  # Return the total number of colors used