'''
Module for calculating the number of safe squares on a grid.
'''
from typing import List, Tuple
def count_safe_squares(N: int, M: int, pieces: List[Tuple[int, int]]) -> int:
    attacked_squares = set()
    # Validate pieces coordinates
    for a_k, b_k in pieces:
        if not (1 <= a_k <= N and 1 <= b_k <= N):
            raise ValueError(f"Piece coordinates ({a_k}, {b_k}) are out of bounds for grid size {N}.")
    for a_k, b_k in pieces:
        # Mark the row
        for j in range(1, N + 1):
            attacked_squares.add((a_k, j))
        # Mark the column
        for i in range(1, N + 1):
            attacked_squares.add((i, b_k))
        # Mark the main diagonal
        for d in range(-N, N + 1):
            if 1 <= a_k + d <= N and 1 <= b_k + d <= N:
                attacked_squares.add((a_k + d, b_k + d))
        # Mark the anti-diagonal
        for d in range(-N, N + 1):
            if 1 <= a_k + d <= N and 1 <= b_k - d <= N:
                attacked_squares.add((a_k + d, b_k - d))
    total_squares = N * N
    safe_squares = total_squares - len(attacked_squares)
    return safe_squares