'''
Grid processing functions for calculating the maximum number from the grid.
'''
def get_max_number(grid, start_row, start_col, direction, n):
    # Check if the starting position is out of bounds
    if not (0 <= start_row < n and 0 <= start_col < n):
        return 0  # Return 0 if starting position is invalid
    collected_digits = []
    row, col = start_row, start_col
    # Check if the entire path remains within bounds
    for step in range(n - 1):  # Iterate N-1 steps
        if 0 <= row < n and 0 <= col < n:
            collected_digits.append(str(grid[row][col]))
            row += direction[0]
            col += direction[1]
        else:
            return 0  # Return 0 if out of bounds at any step
    # Return the integer formed from the collected digits, or 0 if no digits were collected
    return int(''.join(collected_digits)) if collected_digits else 0