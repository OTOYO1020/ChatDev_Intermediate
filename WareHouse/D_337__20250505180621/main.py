'''
Main application file for the Grid Converter application.
'''
import sys
from grid_operations import find_min_operations
def main():
    # Read integers H, W, and K from standard input
    try:
        H, W, K = map(int, input().split())
        if H <= 0 or W <= 0 or K <= 0 or K > W:
            print("Invalid input: H, W, and K must be positive integers, and K must not exceed W.")
            return
    except ValueError:
        print("Please enter valid integers for H, W, and K.")
        return
    # Check for empty grid
    if H == 0:
        print("Grid cannot be empty.")
        return
    # Read H strings representing the grid
    grid = [input().strip() for _ in range(H)]
    if any(len(row) != W for row in grid):
        print(f"Each row must have exactly {W} characters.")
        return
    # Validate grid characters
    for row in grid:
        if any(c not in ('o', 'x') for c in row):  # Assuming 'x' is the other character
            print("Grid can only contain 'o' or 'x'. Please correct your input.")
            return
    # Calculate the minimum operations needed
    min_operations = find_min_operations(grid, H, W, K)
    # Print the result
    print(min_operations)
if __name__ == "__main__":
    main()