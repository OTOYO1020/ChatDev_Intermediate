'''
Module containing matrix operations for isolation checking.
'''
from typing import List, Tuple
def is_isolated(i: int, j: int, A: List[List[int]], H: int, W: int) -> bool:
    # Check if the element A[i][j] is isolated
    if A[i][j] == 0:
        return True
    # Check all 8 possible directions for isolation
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < H and 0 <= nj < W and A[ni][nj] == 1:
            return False
    return True
def min_operations_to_isolate(H: int, W: int, A: List[List[int]]) -> Tuple[bool, int]:
    # Check if the matrix is already non-isolated
    if not any(is_isolated(i, j, A, H, W) for i in range(H) for j in range(W)):
        return (True, 0)
    operations = 0
    while True:
        rows_to_flip = set()
        # Check for isolation
        for i in range(H):
            for j in range(W):
                if is_isolated(i, j, A, H, W):
                    rows_to_flip.add(i)
        # If no rows need to be flipped, break the loop
        if not rows_to_flip:
            break
        # Flip the identified rows
        for i in rows_to_flip:
            A[i] = [1 - A[i][j] for j in range(W)]  # Flip the row
            operations += 1
        # After flipping, check for isolation again
        if not any(is_isolated(i, j, A, H, W) for i in range(H) for j in range(W)):
            return (True, operations)  # Return tuple indicating success and number of operations
    return (False, operations)  # Return tuple indicating failure