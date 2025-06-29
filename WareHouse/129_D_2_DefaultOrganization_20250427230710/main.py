'''
Main application file for the lighting grid application.
'''
import sys
from grid_handler import GridHandler
from utils import validate_input
def main():
    # Input Handling
    h, w = map(int, sys.stdin.readline().strip().split())
    grid = [sys.stdin.readline().strip() for _ in range(h)]
    # Validate input
    if not validate_input(h, w, grid):
        print("Invalid input. Please check your entries.")
        return
    # Initialize GridHandler
    grid_handler = GridHandler(h, w, grid)
    # Calculate light count before getting max lighted squares
    grid_handler.calculate_light_count()
    max_lighted = grid_handler.get_max_lighted_squares()
    # Output the result
    print(max_lighted)
if __name__ == "__main__":
    main()