'''
Contains functions to validate the Sudoku grid.
'''
def is_valid_sudoku(A):
    """
    Check if the Sudoku grid is valid by ensuring all numbers 1-9 appear exactly once
    in each row, column, and 3x3 subgrid.
    """
    expected_set = set(range(1, 10))  # Set of numbers from 1 to 9
    for i in range(9):
        row_seen = set()
        col_seen = set()
        for j in range(9):
            num_row = A[i][j]
            num_col = A[j][i]  # Access the column values correctly
            if num_row < 1 or num_row > 9 or num_col < 1 or num_col > 9:
                return False
            row_seen.add(num_row)
            col_seen.add(num_col)
        if row_seen != expected_set or col_seen != expected_set:
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid_seen = set()
            for x in range(3):
                for y in range(3):
                    num = A[i + x][j + y]
                    if num < 1 or num > 9 or num in subgrid_seen:
                        return False
                    subgrid_seen.add(num)
            if subgrid_seen != expected_set:  # Ensure subgrid contains all numbers from 1 to 9
                return False
    return True