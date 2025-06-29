'''
Main entry point for the grid movement application.
'''
import sys
from grid import Grid  # Importing the Grid class from grid.py
class GridApp:
    def __init__(self):
        self.grid = None
    def setup_grid(self):
        try:
            height = int(input("Enter the number of rows in the grid (H): "))
            width = int(input("Enter the number of columns in the grid (W): "))
        except ValueError:
            print("Error: Please enter valid integers for height and width.")
            return
        configuration = []
        for i in range(height):
            row = input(f"Enter row {i + 1} (use '.' for empty and '#' for blocked): ")
            if len(row) != width or any(c not in ['.', '#'] for c in row):
                print(f"Error: Row {i + 1} must have exactly {width} characters and only '.' or '#' as valid characters.")
                return
            configuration.append(row)
        self.grid = Grid(height, width, configuration)
    def execute_movements(self):
        if self.grid is None:
            print("Error: Please set up the grid first.")
            return
        try:
            start_i = int(input("Enter starting row (S_i): "))
            start_j = int(input("Enter starting column (S_j): "))
        except ValueError:
            print("Error: Please enter valid integers for starting positions.")
            return
        if start_i < 1 or start_i > self.grid.height or start_j < 1 or start_j > self.grid.width:
            print("Error: Starting position is out of bounds.")
            return
        # Check if the starting position is blocked before converting to zero-based indexing
        if self.grid.configuration[start_i - 1][start_j - 1] == '#':
            print(f"Error: Starting position ({start_i}, {start_j}) is blocked. Please choose a different starting position.")
            return
        movements = input("Enter movements (L, R, U, D): ")
        final_position = self.grid.execute_movements(start_i, start_j, movements)
        if final_position is not None:
            print(f"Final Position: {final_position}")
    def run(self):
        self.setup_grid()
        self.execute_movements()
if __name__ == "__main__":
    app = GridApp()
    app.run()