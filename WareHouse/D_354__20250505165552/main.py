'''
Main application file for calculating the area of black regions.
'''
import sys
from black_region import is_black_region
def main():
    try:
        # Read integers A, B, C, and D from standard input
        A, B, C, D = map(int, sys.stdin.readline().strip().split())
        # Validate rectangle dimensions
        if A >= C or B >= D:
            print("Invalid rectangle dimensions. Ensure that A < C and B < D.")
            return
        black_area = 0
        # Loop through all integer coordinates (x, y) within the rectangle
        for x in range(A, C):
            for y in range(B, D):
                if is_black_region(x, y):
                    black_area += 1
        result = 2 * black_area
        print(f"Black Area: {result}")
    except ValueError:
        print("Please enter valid integers.")
if __name__ == "__main__":
    main()