'''
Main application file for the word fitting application.
'''
import sys
from utils import can_fit_in_window, binary_search_min_width  # Correctly importing both functions
def main():
    try:
        # Read integers N and M from standard input
        N, M = map(int, sys.stdin.readline().strip().split())
        # Input validation for N and M
        if N <= 0 or M <= 0:
            raise ValueError("N and M must be positive integers.")
        # Read the widths of words
        widths = list(map(int, sys.stdin.readline().strip().split()))
        if len(widths) != N:
            raise ValueError("The number of widths must match N.")
        # Validate that all widths are positive integers
        if any(width <= 0 for width in widths):
            raise ValueError("All widths must be positive integers.")
        min_width = binary_search_min_width(widths, M)  # Corrected function call
        print(f"The minimum width required is: {min_width}")
    except ValueError as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()