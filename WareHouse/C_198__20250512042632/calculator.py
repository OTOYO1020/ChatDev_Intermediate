'''
Module for calculating the minimum steps required for Takahashi to reach a destination.
'''
import math
def min_steps_to_reach_destination(R: int, X: int, Y: int) -> int:
    '''
    Calculate the minimum number of steps Takahashi needs to reach the point (X, Y)
    from the origin (0, 0) given a step size R.
    Parameters:
    R (int): The step size (must be a positive integer).
    X (int): The X coordinate of the destination.
    Y (int): The Y coordinate of the destination.
    Returns:
    int: The minimum number of steps required to reach the destination.
    '''
    if (X, Y) == (0, 0):
        return 0  # No steps needed if already at the origin
    distance = math.sqrt(X**2 + Y**2)
    steps = math.ceil(distance / R)
    return steps