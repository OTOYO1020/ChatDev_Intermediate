'''
Module for processing the grid and calculating the minimum median.
'''
def get_min_median(grid, n, k):
    '''
    Calculate the minimum median from all K x K sections of the grid.
    Parameters:
    grid (list of list of int): The 2D array representing the grid.
    n (int): The size of the grid (N x N).
    k (int): The size of the pond (K x K).
    Returns:
    float: The minimum median found in the grid.
    '''
    min_median = float('inf')
    for i in range(n - k + 1):
        for j in range(n - k + 1):
            section = extract_section(grid, i, j, k)
            median = find_median(section)
            min_median = min(min_median, median)
    return min_median
def extract_section(grid, start_row, start_col, k):
    '''
    Extract a K x K section from the grid.
    Parameters:
    grid (list of list of int): The 2D array representing the grid.
    start_row (int): The starting row index for the section.
    start_col (int): The starting column index for the section.
    k (int): The size of the pond (K x K).
    Returns:
    list of int: The extracted K x K section as a flat list.
    '''
    section = []
    for i in range(start_row, start_row + k):
        for j in range(start_col, start_col + k):
            section.append(grid[i][j])
    return section
def find_median(section):
    '''
    Find the median of a list of integers.
    Parameters:
    section (list of int): The list of integers to find the median of.
    Returns:
    float: The median value.
    '''
    section.sort()
    length = len(section)
    median_index = length // 2
    # Return the average of the two middle values for even lengths
    if length % 2 == 0:
        return (section[median_index - 1] + section[median_index]) / 2.0  # Return as float
    else:
        return float(section[median_index])  # Ensure the return value is a float