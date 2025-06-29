'''
Contains the logic for calculating the minimum number of dishes that can be eaten.
'''
from typing import List
def min_dishes(N: int, X: int, Y: int, A: List[int], B: List[int]) -> int:
    '''
    Calculate the minimum number of dishes that can be eaten without exceeding sweetness or saltiness thresholds.
    Parameters:
    N (int): Number of dishes
    X (int): Sweetness threshold
    Y (int): Saltiness threshold
    A (List[int]): List of sweetness values
    B (List[int]): List of saltiness values
    Returns:
    int: Minimum number of dishes eaten
    '''
    # Create a list of dishes with their sweetness and saltiness
    dishes = list(zip(A, B))
    # Sort dishes based on sweetness and then saltiness
    dishes.sort(key=lambda dish: (dish[0], dish[1]))  # Sort by sweetness and then saltiness
    total_sweetness = 0
    total_saltiness = 0
    count = 0
    for sweetness, saltiness in dishes:
        if total_sweetness + sweetness <= X and total_saltiness + saltiness <= Y:
            total_sweetness += sweetness
            total_saltiness += saltiness
            count += 1
        # Check if thresholds are exceeded
        if total_sweetness > X or total_saltiness > Y:
            break
    return count