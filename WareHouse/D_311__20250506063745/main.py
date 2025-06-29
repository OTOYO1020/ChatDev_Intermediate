'''
Main entry point for the ice square exploration application.
'''
from grid import Grid
def main():
    # Read dimensions of the grid
    n, m = map(int, input().split())
    # Read the grid layout
    layout = [input().strip() for _ in range(n)]
    # Create a Grid instance
    grid = Grid(n, m, layout)
    # Explore from the starting position (2, 2) as per 0-based index
    count = grid.explore(2, 2)  # Adjusted to 0-based index
    # Print the count of reachable ice squares
    print(count)
if __name__ == "__main__":
    main()