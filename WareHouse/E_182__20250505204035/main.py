'''
Main entry point of the application that handles user interactions for grid illumination.
'''
import sys
from grid import Grid
def main():
    try:
        # Read dimensions of the grid
        H, W = map(int, input().split())
        # Read number of bulbs and blocks
        N, M = map(int, input().split())
        # Input validation for the number of bulbs and blocks
        if N <= 0:
            raise ValueError("Number of bulbs must be greater than zero.")
        if M < 0:
            raise ValueError("Number of blocks cannot be negative.")
        if N > H * W:
            raise ValueError(f"Number of bulbs ({N}) exceeds the total grid positions ({H * W}).")
        grid = Grid(H, W)
        # Read bulb coordinates (adjusting for 1-based to 0-based indexing)
        bulbs = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]
        grid.add_bulbs(bulbs)
        # Read block coordinates (adjusting for 1-based to 0-based indexing)
        blocks = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
        grid.add_blocks(blocks)
        illuminated_count = grid.illuminate()
        # Print the result
        print(illuminated_count)  # Output format as integer count only
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()