'''
Main application file for the Max Number Finder.
'''
import sys
from grid_processing import get_max_number
def get_grid():
    try:
        n = int(input("Enter the size of the grid (N): "))
        if n <= 0:
            raise ValueError("N must be a positive integer.")
        grid = []
        print("Enter the grid (space-separated rows):")
        for _ in range(n):
            row = list(map(int, input().strip().split()))
            if len(row) != n:
                raise ValueError("Each row must contain exactly N integers.")
            if any(d < 0 or d > 9 for d in row):  # Ensure digits are between 0 and 9
                raise ValueError("Each integer must be a digit (0-9).")
            grid.append(row)
        return grid
    except ValueError as e:
        print(f"Input Error: {e}")
        sys.exit(1)
def calculate_max_number(grid):
    max_number = 0
    n = len(grid)
    directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (0, -1),  # Left
        (-1, 0),  # Up
        (1, 1),   # Down-Right
        (1, -1),  # Down-Left
        (-1, 1),  # Up-Right
        (-1, -1)  # Up-Left
    ]
    for row in range(n):
        for col in range(n):
            for direction in directions:
                max_number = max(max_number, get_max_number(grid, row, col, direction, n))
    return max_number
if __name__ == "__main__":
    grid = get_grid()
    max_number = calculate_max_number(grid)
    print(max_number)  # Output the maximum number directly