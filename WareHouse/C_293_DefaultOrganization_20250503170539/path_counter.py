'''
Module for counting paths in a grid.
'''
class PathCounter:
    def __init__(self, grid):
        self.grid = grid
        self.H = len(grid)
        self.W = len(grid[0]) if grid else 0
    def count_paths(self, i, j, visited):
        # Check if the grid is empty or dimensions are invalid
        if not self.grid or self.H == 0 or self.W == 0:
            return 0
        # Check if the starting position is out of bounds
        if i < 0 or i >= self.H or j < 0 or j >= self.W:
            return 0
        # Check if already visited
        if self.grid[i][j] in visited:
            return 0
        # Check if at the bottom-right corner
        if i == self.H - 1 and j == self.W - 1:
            return 1  # Found a valid path to the bottom-right corner
        # Add the current cell's value to the visited set
        visited.add(self.grid[i][j])
        # Recursively count paths from the current cell to the right and down
        total_paths = self.count_paths(i, j + 1, visited) + self.count_paths(i + 1, j, visited)
        # Backtrack: remove the current cell's value from the visited set
        visited.remove(self.grid[i][j])
        return total_paths