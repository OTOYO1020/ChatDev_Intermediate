'''
Grid class for handling grid data and calculating unbalancedness.
'''
class Grid:
    def __init__(self, h, w, a_values, b_values):
        self.h = h
        self.w = w
        self.a = a_values  # Directly assign the 2D list for red values
        self.b = b_values  # Directly assign the 2D list for blue values
    def calculate_unbalancedness(self, red_sum, blue_sum):
        '''Calculate the unbalancedness based on the sums of red and blue numbers.'''
        return abs(red_sum - blue_sum)
    def dfs(self, i, j, red_sum, blue_sum, visited):
        '''Depth-first search to explore all paths and calculate unbalancedness.'''
        # Base case: if we reach the bottom-right corner
        if i == self.h - 1 and j == self.w - 1:
            # Calculate unbalancedness for the final sums
            return self.calculate_unbalancedness(red_sum, blue_sum)
        # If the current cell is already visited, return infinity to avoid cycles
        if (i, j) in visited:
            return float('inf')
        # Mark the current cell as visited
        visited.add((i, j))
        min_unbalancedness = float('inf')
        # Paint the current cell before moving
        # Paint red
        new_red_sum = red_sum + self.a[i][j]
        # Paint blue
        new_blue_sum = blue_sum + self.b[i][j]
        # Move down
        if i + 1 < self.h:
            min_unbalancedness = min(min_unbalancedness, self.dfs(i + 1, j, new_red_sum, blue_sum, visited))
            min_unbalancedness = min(min_unbalancedness, self.dfs(i + 1, j, red_sum, new_blue_sum, visited))
        # Move right
        if j + 1 < self.w:
            min_unbalancedness = min(min_unbalancedness, self.dfs(i, j + 1, new_red_sum, blue_sum, visited))
            min_unbalancedness = min(min_unbalancedness, self.dfs(i, j + 1, red_sum, new_blue_sum, visited))
        # Unmark the current cell as visited before backtracking
        visited.remove((i, j))
        return min_unbalancedness
    def find_min_unbalancedness(self):
        '''Find the minimum unbalancedness by exploring all paths in the grid.'''
        if self.h == 1 and self.w == 1:  # Check for 1x1 grid
            return self.calculate_unbalancedness(self.a[0][0], self.b[0][0])
        red_initial = self.a[0][0]
        blue_initial = self.b[0][0]
        visited = set()  # Initialize the visited set
        return min(
            self.dfs(0, 0, red_initial, 0, visited),  # Start with red at (0, 0)
            self.dfs(0, 0, 0, blue_initial, visited)   # Start with blue at (0, 0)
        )