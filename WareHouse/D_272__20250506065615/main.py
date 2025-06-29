'''
Main entry point for the grid reachability application.
'''
from grid import Grid
def main():
    # Read input values for grid size and distance squared
    N = int(input("Enter grid size (N): "))
    M = int(input("Enter distance squared (M): "))
    grid = Grid(N, M)
    # Print the reachable grid
    print("Reachable Grid:")
    for row in grid.get_reachable():  # No need to skip the first row for 0-based indexing
        print(row)  # No need to skip the first column for 0-based indexing
    # Print the minimum operations grid
    print("Minimum Operations:")
    for row in grid.get_min_operations():  # No need to skip the first row for 0-based indexing
        print(row)  # No need to skip the first column for 0-based indexing
if __name__ == "__main__":
    main()