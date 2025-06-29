'''
Grid class to perform calculations for lighted squares.
'''
class Grid:
    def __init__(self, h, w, grid):
        self.h = h
        self.w = w
        self.grid = grid
        self.light_count = [[0] * w for _ in range(h)]
    def calculate_light_count(self):
        # Reset light count for obstacles at the beginning
        for i in range(self.h):
            for j in range(self.w):
                if self.grid[i][j] == '#':
                    self.light_count[i][j] = 0  # Reset light count for obstacles
                else:
                    self.light_count[i][j] = 0  # Initialize light count for empty squares
        # Horizontal lighting
        for i in range(self.h):
            count = 0
            for j in range(self.w):
                if self.grid[i][j] == '.':
                    count += 1
                    self.light_count[i][j] = count
                else:
                    count = 0  # Reset count for obstacles
            count = 0
            for j in range(self.w - 1, -1, -1):
                if self.grid[i][j] == '.':
                    count += 1
                    self.light_count[i][j] = max(self.light_count[i][j], count)
                else:
                    count = 0  # Reset count for obstacles
        # Vertical lighting
        for j in range(self.w):
            count = 0
            for i in range(self.h):
                if self.grid[i][j] == '.':
                    count += 1
                    self.light_count[i][j] += count  # Correctly add the count
                else:
                    count = 0  # Reset count for obstacles
            count = 0
            for i in range(self.h - 1, -1, -1):
                if self.grid[i][j] == '.':
                    count += 1
                    self.light_count[i][j] += count  # Correctly add the count
                else:
                    count = 0  # Reset count for obstacles
        # Ensure not to double count the square itself
        for i in range(self.h):
            for j in range(self.w):
                if self.grid[i][j] == '.':
                    self.light_count[i][j] -= 1  # Subtract 1 to exclude the square itself
    def get_max_lighted_squares(self):
        max_lighted = 0
        for i in range(self.h):
            for j in range(self.w):
                if self.grid[i][j] == '.':
                    # Always subtract 1 to exclude the square itself
                    max_lighted = max(max_lighted, self.light_count[i][j] - 1)
        return max_lighted