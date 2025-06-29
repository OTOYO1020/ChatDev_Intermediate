'''
Main application file for the Pond Median Calculator.
'''
import sys
from grid_processing import get_min_median
def main():
    try:
        n, k = map(int, input("Enter N (grid size) and K (pond size): ").split())
        if n < 1:
            raise ValueError("N must be a positive integer.")
        if k < 1 or k > n:
            raise ValueError("K must be between 1 and N.")
        grid = []
        print("Enter grid values (space-separated):")
        for _ in range(n):
            row = list(map(int, input().split()))
            if len(row) != n:
                raise ValueError("Grid dimensions do not match N.")
            grid.append(row)
        min_median = get_min_median(grid, n, k)
        print(f"Minimum Median: {min_median}")
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
if __name__ == "__main__":
    main()