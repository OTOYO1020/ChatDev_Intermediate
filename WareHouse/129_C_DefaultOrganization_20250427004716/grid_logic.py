'''
Logic for calculating the maximum number of lighted squares in a grid.
'''
class GridLogic:
    def __init__(self, grid):
        self.grid = grid
        self.H = len(grid)
        self.W = len(grid[0]) if self.H > 0 else 0
        self.light_count = [[0] * self.W for _ in range(self.H)]
        self.calculate_light_count()  # Ensure light_count is calculated upon initialization
    def calculate_light_count(self):
        # Calculate horizontal lighting
        for i in range(self.H):
            count = 0
            for j in range(self.W):
                if self.grid[i][j] == '.':
                    count += 1
                    self.light_count[i][j] = count
                else:
                    count = 0  # Reset count when encountering an obstacle
            count = 0
            for j in range(self.W - 1, -1, -1):
                if self.grid[i][j] == '.':
                    count += 1
                    # Update light_count[i][j] only if it's an empty square
                    self.light_count[i][j] = max(self.light_count[i][j], count)
                else:
                    count = 0  # Reset count when encountering an obstacle
        # Calculate vertical lighting
        for j in range(self.W):
            count = 0  # Start from 0 to count the square itself
            for i in range(self.H):
                if self.grid[i][j] == '.':
                    count += 1
                    # Add to the existing count
                    self.light_count[i][j] += count
                else:
                    count = 0  # Reset count when encountering an obstacle
            count = 0  # Reset for bottom-up traversal
            for i in range(self.H - 1, -1, -1):
                if self.grid[i][j] == '.':
                    count += 1
                    # Update with max from below
                    self.light_count[i][j] = max(self.light_count[i][j], count)
                else:
                    count = 0  # Reset count when encountering an obstacle
    def get_max_lighted(self):
        max_lighted = 0
        # Check if there are any empty squares in the grid
        if all(self.grid[i][j] == '#' for i in range(self.H) for j in range(self.W)):
            print("No empty squares available for lighting.")
            return max_lighted  # Return 0 if no empty squares are present
        for i in range(self.H):
            for j in range(self.W):
                if self.grid[i][j] == '.':
                    # Subtract 1 to exclude the square itself from being counted twice
                    max_lighted = max(max_lighted, self.light_count[i][j] - 1)
        return max_lighted