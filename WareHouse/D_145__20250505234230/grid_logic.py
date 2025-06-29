'''
Contains the logic for calculating the number of ways to reach a target cell in a grid.
'''
class GridLogic:
    MOD = 10**9 + 7  # Modulo value to prevent overflow
    def calculate_ways(self, x, y):
        # Initialize a 1D array to store the number of ways to reach each cell
        ways = [0] * (y + 1)  # Create a 1D array for the current row
        ways[0] = 1  # Starting position has one way to be reached
        # Loop through each cell in the grid
        for i in range(x + 1):
            # Create a temporary array to store the next row's values
            next_ways = [0] * (y + 1)
            for j in range(y + 1):
                # Update the number of ways to reach (i, j)
                next_ways[j] = (next_ways[j] + ways[j]) % self.MOD
                # Update the number of ways to reach (i+1, j+2)
                if i + 1 <= x and j + 2 <= y:
                    next_ways[j + 2] = (next_ways[j + 2] + ways[j]) % self.MOD
                # Update the number of ways to reach (i+2, j+1)
                if i + 2 <= x and j + 1 <= y:
                    next_ways[j + 1] = (next_ways[j + 1] + ways[j]) % self.MOD
            # Move to the next row
            ways = next_ways
        return ways[y]  # Return the number of ways to reach (X, Y)