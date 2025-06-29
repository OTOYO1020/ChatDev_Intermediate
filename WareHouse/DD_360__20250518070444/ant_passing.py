'''
Module for counting passing pairs of ants based on their positions and directions.
'''
from typing import List
def count_passing_pairs(N: int, T: float, S: str, X: List[int]) -> int:
    # Initialize final positions
    final_positions = []
    for i in range(N):
        final_position = X[i] + (1 if S[i] == '1' else -1) * (T + 0.1)
        final_positions.append((final_position, S[i]))
    # Sort final positions
    final_positions.sort()
    # Count passing pairs
    count = 0
    zeros = 0  # Count of '0's seen so far
    for position, direction in final_positions:
        if direction == '0':
            zeros += 1
        else:  # direction == '1'
            count += zeros  # All previous '0's will pass this '1'
    return count