'''
Module for processing grid operations, including shifting outer squares.
'''
def shift_outer_squares(grid):
    N = len(grid)
    if N == 0:  # Handle case when N is 0
        return grid
    if N == 1:  # Handle case when N is 1
        return grid  # No need to shift, just return the grid as is
    outer_squares = []
    # Collect outer squares in clockwise order
    for j in range(N):
        outer_squares.append(grid[0][j])  # Top row
    for i in range(1, N):
        outer_squares.append(grid[i][N-1])  # Right column
    for j in range(N-2, -1, -1):
        outer_squares.append(grid[N-1][j])  # Bottom row
    for i in range(N-2, 0, -1):
        outer_squares.append(grid[i][0])  # Left column
    # Shift outer squares clockwise
    outer_squares = [outer_squares[-1]] + outer_squares[:-1]
    # Update grid with shifted outer squares
    index = 0
    # Update top row
    for j in range(N):
        grid[0][j] = outer_squares[index]
        index += 1
    # Update right column
    for i in range(1, N):
        grid[i][N-1] = outer_squares[index]
        index += 1
    # Update bottom row
    if N > 1:  # Only update if N is greater than 1
        for j in range(N-2, -1, -1):
            grid[N-1][j] = outer_squares[index]
            index += 1
    # Update left column
    if N > 1:  # Only update if N is greater than 1
        for i in range(N-2, 0, -1):
            grid[i][0] = outer_squares[index]
            index += 1
    return grid