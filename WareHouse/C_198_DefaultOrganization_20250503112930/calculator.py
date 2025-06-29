'''
Module for calculating the Euclidean distance and minimum steps.
'''
import math
def calculate_steps(R, X, Y):
    '''
    Calculate the minimum number of steps required to reach the point (X, Y).
    Parameters:
    R (int): The distance that can be covered in one step.
    X (int): The x-coordinate of the target point.
    Y (int): The y-coordinate of the target point.
    Returns:
    int: The minimum number of steps required.
    '''
    D = math.sqrt(X**2 + Y**2)  # Calculate Euclidean distance
    steps = math.ceil(D / R)     # Calculate minimum steps
    return steps