'''
Contains functions to calculate the probability of not getting disappointed.
'''
from typing import List
from collections import Counter
from math import factorial, prod
from itertools import permutations
def check_disappointment(grid: List[List[int]]) -> bool:
    '''
    Determines if Takahashi will be disappointed based on the arrangement of numbers.
    It checks if the first two numbers seen are the same as the third.
    '''
    flat_grid = [num for row in grid for num in row]
    # Check the first three numbers in a fixed order
    first, second, third = flat_grid[0], flat_grid[1], flat_grid[2]
    return first == third or second == third
def calculate_probability(grid: List[List[int]]) -> float:
    '''
    Calculates the probability that Takahashi does not get disappointed based on the arrangement
    of numbers in the grid. It checks for valid configurations and computes the total arrangements
    and non-disappointing arrangements.
    '''
    # Check for invalid grid configurations
    if any(len(set(row)) < 3 for row in grid) or \
       any(len(set(grid[i][j] for i in range(3))) < 3 for j in range(3)) or \
       len(set(grid[i][i] for i in range(3))) < 3 or \
       len(set(grid[i][2-i] for i in range(3))) < 3:
        return 0.0
    # Count occurrences of each number
    flat_grid = [num for row in grid for num in row]
    count = Counter(flat_grid)
    # Calculate total arrangements based on actual counts
    total_arrangements = factorial(len(flat_grid)) // \
        prod(factorial(count[num]) for num in range(1, 10) if count[num] > 0)
    # Generate all unique arrangements of the grid
    unique_permutations = set(permutations(flat_grid))
    non_disappointing_arrangements = sum(
        1 for perm in unique_permutations if not check_disappointment([list(perm[i:i+3]) for i in range(0, 9, 3)])
    )
    return non_disappointing_arrangements / total_arrangements if total_arrangements > 0 else 0.0