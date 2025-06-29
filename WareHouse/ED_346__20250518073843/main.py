'''
Main entry point for the grid painting application.
'''
from grid_painter import paint_grid
from typing import List, Tuple, Dict
def main():
    # Example usage of the paint_grid function
    H = 5  # Height of the grid
    W = 5  # Width of the grid
    M = 3  # Number of operations
    operations: List[Tuple[int, int, int]] = [
        (1, 0, 1),  # Paint row 0 with color 1
        (2, 1, 2),  # Paint column 1 with color 2
        (1, 2, 3)   # Paint row 2 with color 3
    ]
    color_count = paint_grid(H, W, M, operations)
    print(color_count)  # Output the color counts
if __name__ == "__main__":
    main()