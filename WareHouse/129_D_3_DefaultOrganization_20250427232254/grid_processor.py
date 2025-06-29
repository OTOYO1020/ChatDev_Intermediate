'''
Module for processing the grid and calculating the maximum lighted squares.
'''
class GridProcessor:
    def __init__(self, grid):
        self.grid = grid
        self.H = len(grid)
        self.W = len(grid[0]) if self.H > 0 else 0
        self.light_count = [[0] * self.W for _ in range(self.H)]
        self.calculate_light_count()  # Ensure light_count is calculated on initialization
    def calculate_light_count(self):
        # Horizontal lighting
        for i in range(self.H):
            count = 0
            for j in range(self.W):
                if self.grid[i][j] == '.':
                    count += 1
                    self.light_count[i][j] = count
                else:
                    count = 0  # Reset count on obstacle
            count = 0
            for j in range(self.W - 1, -1, -1):
                if self.grid[i][j] == '.':
                    count += 1
                    self.light_count[i][j] = max(self.light_count[i][j], count)
                else:
                    count = 0  # Reset count on obstacle
        # Vertical lighting
        for j in range(self.W):
            count = 0
            for i in range(self.H):
                if self.grid[i][j] == '.':
                    count += 1
                    self.light_count[i][j] += count  # Accumulate counts from vertical lighting
                else:
                    count = 0  # Reset count on obstacle
            count = 0
            for i in range(self.H - 1, -1, -1):
                if self.grid[i][j] == '.':
                    count += 1
                    self.light_count[i][j] = max(self.light_count[i][j], count)  # Correctly update with max from below
                else:
                    count = 0  # Reset count on obstacle
    def get_max_lighted(self):
        max_lighted = 0
        for i in range(self.H):
            for j in range(self.W):
                if self.grid[i][j] == '.':
                    # Update max_lighted with the total light count from this position, excluding the square itself
                    max_lighted = max(max_lighted, self.light_count[i][j] - 1) if self.light_count[i][j] > 0 else max_lighted
        return max_lighted