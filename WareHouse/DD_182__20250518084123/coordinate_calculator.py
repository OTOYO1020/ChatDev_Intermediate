'''
Module containing the function to calculate the greatest coordinate.
'''
from typing import List
def greatest_coordinate(A: List[int]) -> int:
    '''
    Calculates the greatest coordinate occupied by the robot based on the input list.
    Parameters:
    A (List[int]): A list of integers representing the robot's movements.
    Returns:
    int: The greatest coordinate occupied by the robot.
    '''
    if not A:  # Check if the list is empty
        return 0  # Return 0 for empty input
    current_position = 0
    max_position = 0  # Initialize to 0 to handle all negative values correctly
    for move in A:
        current_position += move
        if current_position > max_position:
            max_position = current_position
    return max_position