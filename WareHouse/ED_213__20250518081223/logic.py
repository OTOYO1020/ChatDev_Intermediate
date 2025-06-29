'''
Logic file for calculating the minimum punches needed for Takahashi.
'''
from collections import deque
from typing import List
def min_punches(H: int, W: int, S: List[str]) -> int:
    '''
    Calculate the minimum number of punches needed for Takahashi to reach the fish market.
    Parameters:
    H (int): The height of the grid.
    W (int): The width of the grid.
    S (List[str]): The grid represented as a list of strings.
    Returns:
    int: The minimum number of punches needed to reach the bottom-right corner of the grid.
    '''
    def is_passable(i, j, grid):
        '''
        Check if a cell (i, j) is passable.
        Parameters:
        i (int): The row index of the cell.
        j (int): The column index of the cell.
        grid (List[str]): The current state of the grid.
        Returns:
        bool: True if the cell is passable, False otherwise.
        '''
        return 0 <= i < H and 0 <= j < W and (grid[i][j] == '.')
    def punch_block(grid, i, j):
        '''
        Clear a 2x2 block of cells starting from (i, j).
        Parameters:
        grid (List[str]): The current state of the grid.
        i (int): The row index of the top-left cell of the block.
        j (int): The column index of the top-left cell of the block.
        Returns:
        List[str]: The new grid with the 2x2 block cleared.
        '''
        new_grid = [list(row) for row in grid]
        new_grid[i][j] = '.'
        new_grid[i + 1][j] = '.'
        new_grid[i][j + 1] = '.'
        new_grid[i + 1][j + 1] = '.'
        return [''.join(row) for row in new_grid]
    def simulate_movement():
        '''
        Simulate Takahashi's movement from the top-left to the bottom-right corner of the grid.
        Returns:
        int: The minimum number of punches needed to reach the target cell.
        '''
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque([(0, 0, 0, S)])  # (x, y, punches, current_grid)
        visited = set()
        visited.add((0, 0, 0, tuple(S)))  # Track visited states by (x, y, punches, grid state)
        while queue:
            x, y, punches, current_grid = queue.popleft()
            if x == H - 1 and y == W - 1:
                return punches
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_passable(nx, ny, current_grid):
                    if (nx, ny, punches, tuple(current_grid)) not in visited:
                        visited.add((nx, ny, punches, tuple(current_grid)))
                        queue.append((nx, ny, punches, current_grid))
            # Check for 2x2 blocks that need punches
            for dx in range(2):
                for dy in range(2):
                    if 0 <= x + dx < H - 1 and 0 <= y + dy < W - 1:
                        if (current_grid[x + dx][y + dy] == '#' and 
                            current_grid[x + dx + 1][y + dy] == '#' and 
                            current_grid[x + dx][y + dy + 1] == '#' and 
                            current_grid[x + dx + 1][y + dy + 1] == '#'):
                            new_grid = punch_block(current_grid, x + dx, y + dy)
                            if (x + dx, y + dy, punches + 1, tuple(new_grid)) not in visited:
                                visited.add((x + dx, y + dy, punches + 1, tuple(new_grid)))
                                queue.append((x + dx, y + dy, punches + 1, new_grid))
                                # Allow immediate movement into the newly cleared cells
                                for ddx, ddy in directions:
                                    nnx, nny = x + dx + ddx, y + dy + ddy
                                    if is_passable(nnx, nny, new_grid):
                                        if (nnx, nny, punches + 1, tuple(new_grid)) not in visited:
                                            visited.add((nnx, nny, punches + 1, tuple(new_grid)))
                                            queue.append((nnx, nny, punches + 1, new_grid))
        return -1  # If no path is found
    return simulate_movement()