'''
Contains functions to process the grid and calculate operations.
'''
def count_operations_to_consecutive_o(row, start_col, grid, K):
    operations = 0
    # Ensure that the starting column is within the valid range
    if start_col < 0 or start_col + K > len(grid[row]):
        return float('inf')  # Return a large number if out of bounds
    # Loop through K cells starting from (row, start_col) using zero-based indexing
    for j in range(start_col, start_col + K):  
        if grid[row][j] != 'o':
            operations += 1
    return operations
def count_operations_to_consecutive_o_vertical(start_row, col, grid, K):
    operations = 0
    # Ensure that the starting row is within the valid range
    if start_row < 0 or start_row + K > len(grid):
        return float('inf')  # Return a large number if out of bounds
    # Loop through K cells starting from (start_row, col) using zero-based indexing
    for i in range(start_row, start_row + K):  
        if grid[i][col] != 'o':
            operations += 1
    return operations
def find_min_operations(grid, H, W, K):
    min_operations = float('inf')
    # Check horizontal sequences
    for row in range(H):
        for j in range(W - K + 1):  # Valid starting column range (zero-based indexing)
            operations = count_operations_to_consecutive_o(row, j, grid, K)
            min_operations = min(min_operations, operations)
    # Check vertical sequences
    for col in range(W):
        for i in range(H - K + 1):  # Valid starting row range (zero-based indexing)
            operations = count_operations_to_consecutive_o_vertical(i, col, grid, K)
            min_operations = min(min_operations, operations)
    return min_operations if min_operations != float('inf') else -1