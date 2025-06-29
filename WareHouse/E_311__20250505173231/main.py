'''
Main application file for the holeless squares calculator.
'''
from grid import Grid
def main():
    '''
    Main function to execute the holeless squares calculation.
    '''
    # Read dimensions of the grid
    H, W = map(int, input().split())
    # Create a Grid instance
    grid = Grid(H, W)
    # Read number of holed squares
    N = int(input())
    # Input validation for N
    if N < 0:
        print("Error: The number of holed squares cannot be negative.")
        return
    # Read coordinates of holed squares
    for _ in range(N):
        a, b = map(int, input().split())
        a -= 1  # Adjust for zero-indexing
        b -= 1  # Adjust for zero-indexing
        if 0 <= a < H and 0 <= b < W:  # Validate coordinates
            grid.add_hole((a, b))  # Updated to add a single hole
        else:
            print(f"Warning: Coordinates ({a + 1}, {b + 1}) are out of bounds and will be ignored.")  # Original input coordinates
    # Count holeless squares using the Grid class method
    holeless_count = grid.count_holeless_squares()
    # Print the result
    print(holeless_count)
if __name__ == "__main__":
    main()