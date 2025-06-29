'''
Module to calculate the minimum unbalancedness between two grids.
'''
from typing import List
def min_unbalancedness(H: int, W: int, A: List[List[int]], B: List[List[int]]) -> int:
    min_unbalanced = float('inf')
    def explore(i: int, j: int, red_sum: int, blue_sum: int):
        nonlocal min_unbalanced  # Ensure this is declared at the start of the function
        # Base case: if we reach the bottom-right corner of the grid
        if i == H - 1 and j == W - 1:
            unbalancedness = abs(red_sum - blue_sum)
            min_unbalanced = min(min_unbalanced, unbalancedness)  # Correctly update minimum unbalancedness
            return
        # Move down if within bounds
        if i < H - 1:
            # Explore painting current cell A[i][j] red and B[i][j] blue
            explore(i + 1, j, red_sum + A[i][j], blue_sum + B[i][j])
            # Explore painting current cell A[i][j] blue and B[i][j] red
            explore(i + 1, j, red_sum + B[i][j], blue_sum + A[i][j])
        # Move right if within bounds
        if j < W - 1:
            # Explore painting current cell A[i][j] red and B[i][j] blue
            explore(i, j + 1, red_sum + A[i][j], blue_sum + B[i][j])
            # Explore painting current cell A[i][j] blue and B[i][j] red
            explore(i, j + 1, red_sum + B[i][j], blue_sum + A[i][j])
    explore(0, 0, 0, 0)
    return min_unbalanced