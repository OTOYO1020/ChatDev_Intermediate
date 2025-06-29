'''
Grid management functions for the Wall Destroyer application.
'''
from typing import List, Tuple
def destroy_first_wall(grid, R_q, C_q, dr, dc):
    '''
    Helper function to find and destroy the first wall in a given direction.
    Parameters:
    grid (List[List[int]]): The grid representing walls.
    R_q (int): The row index of the query.
    C_q (int): The column index of the query.
    dr (int): The change in row index for the direction.
    dc (int): The change in column index for the direction.
    Returns:
    bool: True if a wall was destroyed, False otherwise.
    '''
    # Check if the queried position is within bounds
    if not (0 <= R_q < len(grid) and 0 <= C_q < len(grid[0])):
        return False  # Out of bounds, cannot destroy a wall
    # Check the queried position first
    if grid[R_q][C_q] == 1:
        grid[R_q][C_q] = 0  # Destroy the wall
        return True  # Indicate that a wall was destroyed
    r, c = R_q, C_q
    while True:
        r += dr
        c += dc
        if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):  # Check bounds
            break
        if grid[r][c] == 1:  # Found a wall
            grid[r][c] = 0  # Destroy the wall
            return True  # Indicate that a wall was destroyed
        elif grid[r][c] == 0:  # No wall, stop searching in this direction
            break
    return False  # Indicate that no wall was destroyed
def count_remaining_walls(H: int, W: int, Q: int, queries: List[Tuple[int, int]]) -> int:
    '''
    Initializes a grid of size H x W filled with walls and processes the queries to destroy walls.
    Parameters:
    H (int): Height of the grid.
    W (int): Width of the grid.
    Q (int): Number of queries.
    queries (List[Tuple[int, int]]): List of queries containing the coordinates to process.
    Returns:
    int: Number of remaining walls in the grid.
    '''
    # Initialize the grid with walls (1 represents a wall)
    grid = [[1 for _ in range(W)] for _ in range(H)]
    valid_queries = 0  # Count of valid queries
    for R_q, C_q in queries:
        R_q -= 1  # Adjust for 0-based indexing
        C_q -= 1  # Adjust for 0-based indexing
        if not (0 <= R_q < H and 0 <= C_q < W):  # Check if the query is within bounds
            print(f"Query ({R_q + 1}, {C_q + 1}) is out of bounds and will be skipped.")  # User feedback
            continue  # Skip this query if it's out of bounds
        valid_queries += 1  # Increment valid query count
        if grid[R_q][C_q] == 1:
            grid[R_q][C_q] = 0  # Destroy the wall at (R_q, C_q)
        else:
            # Check adjacent cells in all four directions only if the wall was not destroyed
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
            wall_destroyed = False
            for dr, dc in directions:
                if destroy_first_wall(grid, R_q, C_q, dr, dc):
                    wall_destroyed = True
                    break  # Stop checking other directions if a wall was destroyed
    # Count and return the number of remaining walls
    return sum(cell == 1 for row in grid for cell in row)