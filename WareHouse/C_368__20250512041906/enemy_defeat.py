'''
Module to calculate the time taken to defeat enemies based on their health.
'''
from typing import List
def calculate_time_to_defeat_enemies(N: int, H: List[int]) -> int:
    '''
    Calculate the time taken to defeat all enemies based on their health.
    Parameters:
    N (int): Number of enemies.
    H (List[int]): List of health values for each enemy.
    Returns:
    int: Time taken to defeat all enemies.
    '''
    T = 0  # Initialize time taken to 0
    while H:  # Continue until there are no enemies left
        T += 1  # Increment time
        if T % 3 == 0:  # Check if T is a multiple of 3
            if H[0] > 0:  # Only attack if the frontmost enemy is alive
                H[0] -= 3  # Decrease health by 3
            if H[0] <= 0:  # Check if the frontmost enemy is defeated
                H.pop(0)  # Remove the defeated enemy
    return T  # Return the total time taken