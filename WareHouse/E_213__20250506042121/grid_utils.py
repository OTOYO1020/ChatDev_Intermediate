'''
Utility functions for grid processing in the Takahashi Punches Calculator.
'''
from collections import deque
def can_reach_market(S, H, W):
    '''
    Check if Takahashi can reach the fish market without any punches.
    Parameters:
    S (list of str): The grid representation.
    H (int): The number of rows in the grid.
    W (int): The number of columns in the grid.
    Returns:
    bool: True if the market is reachable, False otherwise.
    '''
    visited = [[False] * W for _ in range(H)]
    queue = deque([(0, 0)])  # Start from the top-left corner
    visited[0][0] = True
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    while queue:
        x, y = queue.popleft()
        if x == H - 1 and y == W - 1:  # Reached the market
            return True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and S[nx][ny] == '.':
                visited[nx][ny] = True
                queue.append((nx, ny))
    return False
def min_punches_needed(S, H, W):
    '''
    Calculate the minimum number of punches needed for Takahashi to reach the market.
    Parameters:
    S (list of str): The grid representation.
    H (int): The number of rows in the grid.
    W (int): The number of columns in the grid.
    Returns:
    int: The minimum number of punches needed, or -1 if unreachable.
    '''
    if can_reach_market(S, H, W):
        return 0  # No punches needed
    min_punches = float('inf')
    # Loop to simulate punching 2x2 blocks
    for i in range(H - 1):
        for j in range(W - 1):
            # Check if we can punch the 2x2 block starting at (i, j)
            if (S[i][j] == '#' and S[i][j + 1] == '#' and 
                S[i + 1][j] == '#' and S[i + 1][j + 1] == '#'):
                # Create a new grid with the punched block
                new_grid = [list(row) for row in S]
                new_grid[i][j] = '.'
                new_grid[i][j + 1] = '.'
                new_grid[i + 1][j] = '.'
                new_grid[i + 1][j + 1] = '.'
                # Check if the market is reachable now
                if can_reach_market(new_grid, H, W):
                    # Update min_punches with the current punch count
                    min_punches = min(min_punches, 1)  # Each punch is counted as 1
    # If no punches were found to make the market reachable, return -1
    return min_punches if min_punches != float('inf') else -1