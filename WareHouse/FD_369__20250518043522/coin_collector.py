'''
Module for calculating maximum coins collected on a grid.
'''
from typing import List, Tuple
def max_coins(H: int, W: int, N: int, coins: List[Tuple[int, int]]) -> Tuple[int, List[Tuple[int, int]]]:
    # Handle the case where there are no coins
    if N == 0:
        return 0, []  # Return empty path if no coins are present
    # Initialize the grid and coin positions
    grid = [[0] * (W + 1) for _ in range(H + 1)]
    for r, c in coins:
        grid[r][c] = 1  # Mark the position of coins
    # Create a DP table to store the maximum coins collected
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    path = [[None] * (W + 1) for _ in range(H + 1)]
    # Fill the DP table
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            coin_value = grid[i][j]
            if i == 1 and j == 1:
                dp[i][j] = coin_value  # Initialize starting point
            else:
                if i > 1 and dp[i][j] < dp[i - 1][j] + coin_value:
                    dp[i][j] = dp[i - 1][j] + coin_value
                    path[i][j] = (i - 1, j)
                if j > 1 and dp[i][j] < dp[i][j - 1] + coin_value:
                    dp[i][j] = dp[i][j - 1] + coin_value
                    path[i][j] = (i, j - 1)
    # Backtrack to find the path
    max_coins_collected = dp[H][W]
    current = (H, W)
    path_taken = []
    # Only backtrack if we have collected any coins
    if max_coins_collected > 0:
        while current:
            path_taken.append(current)
            current = path[current[0]][current[1]]
    path_taken.reverse()
    return max_coins_collected, path_taken
def input_validation(H: int, W: int, N: int, coins: List[Tuple[int, int]]):
    if H <= 0 or W <= 0:
        raise ValueError("Height and Width must be positive integers.")
    if N < 0:
        raise ValueError("Number of coins cannot be negative.")
    if len(coins) != N:
        raise ValueError(f"Expected {N} coin positions, but got {len(coins)}.")
    seen_positions = set()
    for r, c in coins:
        if r < 1 or r > H or c < 1 or c > W:
            raise ValueError(f"Coin position ({r}, {c}) is out of bounds.")
        if (r, c) in seen_positions:
            raise ValueError(f"Duplicate coin position found: ({r}, {c}).")
        seen_positions.add((r, c))