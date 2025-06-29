'''
Contains the logic for counting valid Y positions for the white pawn.
'''
from typing import List, Tuple
def count_possible_Y(N: int, M: int, black_pawns: List[Tuple[int, int]]) -> int:
    # Initialize a grid representation to track black pawn positions
    grid = [[0] * (N + 1) for _ in range(2 * N + 1)]
    for x, y in black_pawns:
        grid[x][y] = 1  # Mark black pawn positions
    # Initialize the starting position of the white pawn
    current_positions = {N}  # Starting at (0, N)
    # Iterate through each row until the last row (2N)
    for i in range(2 * N):  # Iterate through rows 0 to 2N-1
        next_positions = set()
        for j in current_positions:
            # Move down
            if i + 1 < len(grid) and j <= N and grid[i + 1][j] == 0:
                next_positions.add(j)
            # Move diagonally left
            if j - 1 >= 0 and i + 1 < len(grid):
                if grid[i + 1][j - 1] == 0:  # No black pawn
                    next_positions.add(j - 1)
                elif grid[i + 1][j - 1] == 1:  # Capture black pawn
                    next_positions.add(j - 1)  # Allow capturing
                    grid[i + 1][j - 1] = 0  # Mark as empty after capturing
            # Move diagonally right
            if j + 1 <= N and i + 1 < len(grid):
                if grid[i + 1][j + 1] == 0:  # No black pawn
                    next_positions.add(j + 1)
                elif grid[i + 1][j + 1] == 1:  # Capture black pawn
                    next_positions.add(j + 1)  # Allow capturing
                    grid[i + 1][j + 1] = 0  # Mark as empty after capturing
        current_positions = next_positions
    # Count valid Y positions in the last row (2N)
    valid_y_count = sum(1 for j in current_positions if j <= N)
    return valid_y_count