'''
Module to manage the grid and find the missing cookie.
'''
from typing import List, Tuple
def find_eaten_cookie(H: int, W: int, grid: List[List[str]]) -> Tuple[int, int]:
    '''
    Find the coordinates of the missing cookie in the grid.
    Parameters:
    H (int): Height of the grid.
    W (int): Width of the grid.
    grid (List[List[str]]): The grid representation with cookies ('C') and empty spaces ('.').
    Returns:
    Tuple[int, int]: Coordinates of the missing cookie or (-1, -1) if no missing cookie is found.
    '''
    a, b, c, d = None, None, None, None  # Initialize boundaries to None
    total_cookies = 0
    # Find the rectangle boundaries
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 'C':
                total_cookies += 1
                if a is None:  # First cookie found
                    a, c = i, j
                b = i  # Update bottom boundary
                d = j if d is None else max(d, j)  # Update right boundary
                if c is None or j < c:
                    c = j  # Update left boundary
    # Check for presence of cookies
    if total_cookies == 0:
        return (-1, -1)  # No cookies present in the grid
    # Validate rectangle dimensions
    if a is None or b is None or c is None or d is None or (b - a + 1 < 2) or (d - c + 1 < 2):
        return (-1, -1)  # Indicate no missing cookie found
    expected_cookies = (b - a + 1) * (d - c + 1)
    # Check for missing cookie
    if total_cookies < expected_cookies:
        for i in range(a, b + 1):
            for j in range(c, d + 1):
                if grid[i][j] == '.':
                    return (i, j)
    return (-1, -1)  # Indicate no missing cookie found if no empty space is found
class GridManager:
    '''
    Class to manage the grid and find the missing cookie.
    '''
    def process_grid(self, grid_data: List[str]) -> Tuple[int, int]:
        '''
        Process the grid input and find the missing cookie.
        Parameters:
        grid_data (List[str]): The grid input as a list of strings.
        Returns:
        Tuple[int, int]: Coordinates of the missing cookie or (-1, -1) if no missing cookie is found.
        '''
        if not grid_data:  # Check for empty grid
            raise ValueError("Grid cannot be empty.")
        H = len(grid_data)
        W = len(grid_data[0]) if H > 0 else 0
        # Validate grid characters and consistent row lengths
        for row in grid_data:
            if len(row) != W:  # Check for consistent row lengths
                raise ValueError("All rows in the grid must have the same length.")
            if any(char not in ['C', '.'] for char in row):
                raise ValueError("Grid contains invalid characters. Only 'C' and '.' are allowed.")
        grid = [list(row) for row in grid_data]  # Convert to list of lists after validation
        # Check for at least two cookies in the grid
        total_cookies = sum(row.count('C') for row in grid)
        if total_cookies < 2:
            return (-1, -1)  # Not enough cookies to find a missing one
        return find_eaten_cookie(H, W, grid)