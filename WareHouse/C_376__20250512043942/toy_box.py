'''
Module for calculating the minimum box size needed to store toys.
'''
from typing import List
def min_box_size(N: int, A: List[int], B: List[int]) -> int:
    if N == 0:  # If there are no toys
        return 0  # Return 0 as no box size is needed
    A.sort()  # Sort toy sizes in non-decreasing order
    B.sort()  # Sort box sizes in non-decreasing order
    if not B:  # If there are no boxes available
        return A[-1]  # Return the size of the largest toy
    max_toy_size = A[-1]  # Get the maximum size of the toys
    box_index = 0  # Initialize box index
    for toy_size in A:
        # Find a box that can fit the current toy
        while box_index < len(B) and B[box_index] < toy_size:
            box_index += 1
        # If no box can fit the current toy
        if box_index == len(B):
            return toy_size  # Return the size of the current toy needed for a new box
        # Move to the next box for the next toy
        box_index += 1
    # If all toys can be accommodated, return -1
    return -1