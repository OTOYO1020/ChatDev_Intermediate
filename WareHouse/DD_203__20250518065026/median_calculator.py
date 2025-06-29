'''
Module for calculating the minimum median from KxK subgrids in an NxN grid.
'''
from typing import List
def find_minimum_median(N: int, K: int, A: List[List[int]]) -> float:  # Change return type to float
    # Validate grid dimensions
    if len(A) != N or any(len(row) != N for row in A):
        raise ValueError("Grid A must be of size N x N.")
    if N <= 0 or K <= 0 or K > N:
        raise ValueError("N and K must be positive integers, and K must be less than or equal to N.")
    def get_subgrid(x: int, y: int) -> List[int]:
        # Validate subgrid boundaries before accessing the grid
        if x + K > N or y + K > N:
            raise ValueError("Subgrid exceeds grid boundaries.")
        return [A[i][j] for i in range(x, x + K) for j in range(y, y + K)]
    def calculate_median_of_list(lst: List[int]) -> float:  # Ensure return type is float
        if not lst:  # Check if the list is empty
            raise ValueError("The list for median calculation is empty.")
        lst.sort()
        mid = len(lst) // 2
        if len(lst) % 2 == 0:
            return (lst[mid - 1] + lst[mid]) / 2.0  # Use float division
        else:
            return float(lst[mid])  # Ensure the return type is float
    min_median = float('inf')
    for i in range(N - K + 1):
        for j in range(N - K + 1):
            subgrid = get_subgrid(i, j)
            median = calculate_median_of_list(subgrid)
            min_median = min(min_median, median)
    return min_median  # Return as float to maintain precision