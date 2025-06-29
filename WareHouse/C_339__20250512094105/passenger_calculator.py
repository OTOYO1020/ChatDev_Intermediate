'''
Module containing the function to calculate minimum passengers on the bus.
'''
from typing import List
def minimum_passengers(N: int, A: List[int]) -> int:
    '''
    Calculates the minimum possible current number of passengers on the bus.
    Parameters:
    N (int): The number of stops.
    A (List[int]): A list of integers representing changes in the number of passengers at each stop.
    Returns:
    int: The minimum possible current number of passengers, ensuring it is non-negative.
    '''
    current_passengers = 0
    min_passengers = float('inf')  # Initialize to infinity to track minimum correctly
    for change in A:
        current_passengers += change
        min_passengers = min(min_passengers, current_passengers)
    return max(0, -min_passengers)  # Ensure non-negative result