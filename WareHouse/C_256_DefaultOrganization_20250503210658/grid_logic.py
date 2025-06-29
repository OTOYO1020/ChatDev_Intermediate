'''
Module containing the logic for counting valid configurations in a 3x3 grid.
'''
def count_ways(h, w):
    '''
    Counts the number of ways to fill a 3x3 grid based on row sums h and column sums w.
    '''
    grid = [[0] * 3 for _ in range(3)]
    current_col_sums = [0] * 3  # Initialize current column sums
    return backtrack(grid, h, w, 0, 0, current_col_sums)
def backtrack(grid, h, w, row, col, current_col_sums):
    '''
    Recursive backtracking function to fill the grid and count valid configurations.
    '''
    if row == 3:
        # Check if all row and column sums are satisfied
        return 1 if all(sum(grid[i]) == h[i] for i in range(3)) and all(current_col_sums[j] == w[j] for j in range(3)) else 0
    if col == 3:
        return backtrack(grid, h, w, row + 1, 0, current_col_sums)
    count = 0
    max_value = min(h[row] - sum(grid[row]), w[col] - current_col_sums[col])
    # Allow for max_value to be zero but ensure we still explore possibilities
    for value in range(1, max_value + 1):
        grid[row][col] = value
        current_col_sums[col] += value
        if sum(grid[row]) <= h[row] and current_col_sums[col] <= w[col]:  
            count += backtrack(grid, h, w, row, col + 1, current_col_sums)
        current_col_sums[col] -= value
        grid[row][col] = 0  # Reset the cell after backtracking
    return count