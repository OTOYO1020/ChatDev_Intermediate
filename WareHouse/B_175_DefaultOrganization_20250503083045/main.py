'''
Main entry point for the Triangle Combination Calculator application.
'''
import sys
from triangle_calculator import count_valid_triangles
def main():
    try:
        # Read the number of sticks
        N = int(input("Enter the number of sticks (positive integer): "))
        if N <= 0:
            print("Please enter a positive integer for the number of sticks.")
            return
        # Read stick lengths
        lengths = list(map(int, input(f"Enter {N} positive stick lengths (space-separated): ").split()))
        if len(lengths) != N:
            print(f"Please enter exactly {N} lengths.")
            return
        if any(length <= 0 for length in lengths):
            print("All stick lengths must be positive integers.")
            return
        count = count_valid_triangles(lengths)
        print(count)  # Output the count as a single integer without additional message
    except ValueError:
        print("Please enter valid integers.")
if __name__ == "__main__":
    main()