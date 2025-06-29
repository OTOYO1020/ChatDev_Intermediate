'''
Main application file for calculating minimum unbalancedness in a grid.
'''
import sys
from grid import Grid
def main():
    try:
        # Read dimensions from standard input
        h, w = map(int, input("Enter height (H) and width (W): ").split())
        # Initialize lists A and B
        a_values = []
        b_values = []
        # Populate lists A and B
        print("Enter grid A values (row by row):")
        for _ in range(h):
            row = list(map(int, input().split()))
            a_values.append(row)  # Maintain 2D structure
        print("Enter grid B values (row by row):")
        for _ in range(h):
            row = list(map(int, input().split()))
            b_values.append(row)  # Maintain 2D structure
        grid = Grid(h, w, a_values, b_values)
        min_unbalancedness = grid.find_min_unbalancedness()
        print(f"Minimum Unbalancedness: {min_unbalancedness}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
if __name__ == "__main__":
    main()