'''
GridHandler class to manage grid data and calculations for lighting.
'''
class GridHandler:
    def __init__(self, h, w, grid):
        self.h = h
        self.w = w
        self.grid = grid
        self.light_count = [[0] * w for _ in range(h)]
    def calculate_light_count(self):
        # Horizontal lighting
        for i in range(self.h):
            count = 0
            # Left to right
            for j in range(self.w):
                if self.grid[i][j] == '.':
                    count += 1
                    self.light_count[i][j] = count  # Keep the count as is
                else:
                    count = 0  # Reset count on obstacle
            count = 0
            # Right to left
            for j in range(self.w - 1, -1, -1):
                if self.grid[i][j] == '.':
                    count += 1
                    self.light_count[i][j] = max(self.light_count[i][j], count)  # Keep the count as is
                else:
                    count = 0  # Reset count on obstacle
        # Vertical lighting
        for j in range(self.w):
            count = 0
            # Top to bottom
            for i in range(self.h):
                if self.grid[i][j] == '.':
                    count += 1
                    self.light_count[i][j] += count  # Keep the count as is
                else:
                    count = 0  # Reset count on obstacle
            count = 0
            # Bottom to top
            for i in range(self.h - 1, -1, -1):
                if self.grid[i][j] == '.':
                    count += 1
                    self.light_count[i][j] = max(self.light_count[i][j], count)  # Keep the count as is
                else:
                    count = 0  # Reset count on obstacle
    def get_max_lighted_squares(self):
        max_lighted = 0
        for i in range(self.h):
            for j in range(self.w):
                if self.grid[i][j] == '.':
                    # Only consider light count if the square is lightable
                    max_lighted = max(max_lighted, self.light_count[i][j] - 1)  # Subtract 1 to exclude the square itself
        return max_lighted