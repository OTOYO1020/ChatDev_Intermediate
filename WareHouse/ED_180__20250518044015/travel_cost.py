'''
Module for calculating the minimum travel cost between cities.
'''
from itertools import permutations
from typing import List, Tuple
def travel_cost(a: Tuple[int, int, int], b: Tuple[int, int, int]) -> int:
    """
    Calculate the travel cost between two cities based on the Manhattan distance formula.
    Parameters:
    a (Tuple[int, int, int]): Coordinates of the first city (X, Y, Z).
    b (Tuple[int, int, int]): Coordinates of the second city (X, Y, Z).
    Returns:
    int: The calculated travel cost based on the specified formula.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])  # Manhattan distance
def minimum_travel_cost(N: int, coordinates: List[Tuple[int, int, int]]) -> int:
    if N < 2:
        raise ValueError("At least two cities are required.")
    min_cost = float('inf')
    for perm in permutations(coordinates[1:]):  # Exclude the first city
        route = [coordinates[0]] + list(perm) + [coordinates[0]]  # Start and end at City 1
        total_cost = sum(travel_cost(route[i], route[i + 1]) for i in range(len(route) - 1))
        min_cost = min(min_cost, total_cost)
    return int(min_cost)  # Convert to integer before returning