'''
Module for counting distinct paths in a grid.
'''
from typing import List
def count_happy_paths(H: int, W: int, A: List[List[int]]) -> int:
    # Handle edge cases for empty grid
    if H <= 0 or W <= 0:
        return 0
    if H == 1 and W == 1:
        return 1
    memo = {}
    def is_distinct_path(path: List[int]) -> bool:
        # Check if all values in the path are distinct
        return len(path) == len(set(path))
    def find_paths(i: int, j: int, distinct_values: set) -> int:
        # Create a unique key for memoization using the current position and distinct values
        memo_key = (i, j, frozenset(distinct_values))
        if memo_key in memo:
            return memo[memo_key]
        current_value = A[i][j]
        # Check if the current value is distinct
        if current_value in distinct_values:
            return 0  # Not a distinct path
        # Add current value to the set of distinct values
        distinct_values.add(current_value)
        count = 0
        # Check if we have reached the destination
        if i == H - 1 and j == W - 1:
            count += 1  # Found a valid distinct path
        else:
            if i + 1 < H:  # Move down
                count += find_paths(i + 1, j, distinct_values.copy())  # Pass a copy of the distinct values
            if j + 1 < W:  # Move right
                count += find_paths(i, j + 1, distinct_values.copy())  # Pass a copy of the distinct values
        distinct_values.remove(current_value)  # Backtrack
        memo[memo_key] = count  # Store the count with the new key
        return count
    return find_paths(0, 0, set())