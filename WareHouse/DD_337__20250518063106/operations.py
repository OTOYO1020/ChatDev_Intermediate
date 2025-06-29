'''
Module containing the function to calculate the minimum operations
to create K consecutive 'o's in a grid.
'''
from typing import List
def min_operations_to_consecutive_o(H: int, W: int, K: int, S: List[str]) -> int:
    # Check if it's possible to have K consecutive 'o's
    if K > H and K > W:  # Corrected condition
        return -1
    min_operations = float('inf')
    # Check horizontal sequences
    for row in S:
        for start in range(W - K + 1):
            operations_needed = sum(1 for c in row[start:start + K] if c == '.')
            min_operations = min(min_operations, operations_needed)
    # Check vertical sequences
    for col in range(W):
        for start in range(H - K + 1):
            operations_needed = sum(1 for row in range(start, start + K) if S[row][col] == '.')
            min_operations = min(min_operations, operations_needed)
    return min_operations if min_operations != float('inf') else -1