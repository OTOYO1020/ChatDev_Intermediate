'''
Module containing functions to validate a Sudoku grid.
'''
from typing import List
def is_valid_sudoku(grid: List[List[int]]) -> str:
    '''
    Check if the given 9x9 grid satisfies the Sudoku conditions.
    Parameters:
    grid (List[List[int]]): A 9x9 grid of integers representing the Sudoku board.
    Returns:
    str: "Yes" if the grid is a valid Sudoku, "No" otherwise.
    '''
    if not check_rows(grid):
        return "No"
    if not check_columns(grid):
        return "No"
    if not check_subgrids(grid):
        return "No"
    return "Yes"
def check_rows(grid: List[List[int]]) -> bool:
    '''
    Verify that each row contains the integers 1 to 9 exactly once.
    Parameters:
    grid (List[List[int]]): A 9x9 grid of integers representing the Sudoku board.
    Returns:
    bool: True if all rows are valid, False otherwise.
    '''
    for row in grid:
        if set(row) != set(range(1, 10)):  # Check for unique numbers 1-9
            return False
    return True
def check_columns(grid: List[List[int]]) -> bool:
    '''
    Verify that each column contains the integers 1 to 9 exactly once.
    Parameters:
    grid (List[List[int]]): A 9x9 grid of integers representing the Sudoku board.
    Returns:
    bool: True if all columns are valid, False otherwise.
    '''
    for col in range(9):
        column = [grid[row][col] for row in range(9)]
        if set(column) != set(range(1, 10)):  # Check for unique numbers 1-9
            return False
    return True
def check_subgrids(grid: List[List[int]]) -> bool:
    '''
    Verify that each 3x3 subgrid contains the integers 1 to 9 exactly once.
    Parameters:
    grid (List[List[int]]): A 9x9 grid of integers representing the Sudoku board.
    Returns:
    bool: True if all subgrids are valid, False otherwise.
    '''
    for box_row in range(3):
        for box_col in range(3):
            subgrid = []
            for i in range(3):
                for j in range(3):
                    subgrid.append(grid[box_row * 3 + i][box_col * 3 + j])
            if set(subgrid) != set(range(1, 10)):  # Check for unique numbers 1-9
                return False
    return True