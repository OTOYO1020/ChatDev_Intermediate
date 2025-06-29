'''
GridManager class that manages the grid of walls and processes bomb placement queries.
'''
class GridManager:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = [[True for _ in range(width)] for _ in range(height)]
    def destroy_wall(self, r, c):
        self.grid[r][c] = False
    def process_query(self, query):
        try:
            r, c = map(int, query)  # Convert input to integers
            r -= 1  # Adjust for 0-indexing
            c -= 1  # Adjust for 0-indexing
            # Input validation
            if not (0 <= r < self.height and 0 <= c < self.width):
                print("Coordinates out of bounds. Please enter valid coordinates.")
                return
        except ValueError:
            print("Invalid input. Please enter integer values for coordinates.")
            return
        # Check if there is a wall at the specified coordinates
        if self.grid[r][c]:  # If there is a wall, destroy it
            self.destroy_wall(r, c)
        else:  # If there is no wall, check in all four directions
            # Up
            for i in range(r - 1, -1, -1):
                if self.grid[i][c]:
                    self.destroy_wall(i, c)
                    return  # Stop after destroying the first wall
            # Down
            for i in range(r + 1, self.height):
                if self.grid[i][c]:
                    self.destroy_wall(i, c)
                    return  # Stop after destroying the first wall
            # Left
            for j in range(c - 1, -1, -1):
                if self.grid[r][j]:
                    self.destroy_wall(r, j)
                    return  # Stop after destroying the first wall
            # Right
            for j in range(c + 1, self.width):
                if self.grid[r][j]:
                    self.destroy_wall(r, j)
                    return  # Stop after destroying the first wall
    def count_remaining_walls(self):
        # Count the number of walls remaining in the grid (True values)
        return sum(wall for row in self.grid for wall in row)