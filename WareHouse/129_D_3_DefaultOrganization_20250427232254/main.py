'''
Main application file for the lighted squares calculation application.
'''
import sys
from grid_processor import GridProcessor
class MainApp:
    def __init__(self):
        self.run()
    def run(self):
        # Input for grid dimensions
        try:
            H = int(input("Enter number of rows (H): "))
            W = int(input("Enter number of columns (W): "))
            print("Enter grid layout (use '#' for obstacles and '.' for empty squares):")
            grid_input = [input().strip() for _ in range(H)]
            if len(grid_input) != H or any(len(row) != W for row in grid_input):
                raise ValueError("Grid dimensions do not match the input.")
            if any(char not in '#.' for row in grid_input for char in row):
                raise ValueError("Grid can only contain '#' and '.' characters.")
            grid_processor = GridProcessor(grid_input)
            max_lighted = grid_processor.get_max_lighted()
            print(f"Maximum lighted squares: {max_lighted}")
        except Exception as e:
            print(f"Error: {str(e)}", file=sys.stderr)
if __name__ == "__main__":
    MainApp()