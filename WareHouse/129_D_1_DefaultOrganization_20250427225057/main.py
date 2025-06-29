'''
Main entry point for the lighted squares application.
'''
from grid import Grid  # Import the Grid class
def main():
    # Input Handling
    H, W = map(int, input("Enter number of rows (H) and columns (W): ").split())
    grid = [input(f"Enter row {i + 1} of the grid: ") for i in range(H)]
    # Initialize Grid object
    grid_obj = Grid(H, W, grid)
    # Calculate light counts
    grid_obj.calculate_light_count()
    # Calculate Maximum Lighted Squares
    max_lighted = grid_obj.get_max_lighted_squares()
    # Output the Result
    print(f"Maximum Lighted Squares: {max_lighted}")
if __name__ == "__main__":
    main()