'''
Main entry point of the jewels application.
'''
import sys
from jewels import max_blue_jewels
def main():
    try:
        # Read integers N, X, and Y from standard input
        N = int(input("Enter N (1-10): "))
        X = int(input("Enter X (blue jewels from red): "))
        Y = int(input("Enter Y (blue jewels from blue): "))
        # Calculate the maximum number of blue jewels of level 1
        result = max_blue_jewels(N, X, Y)
        # Print the result
        print(f"Maximum Blue Jewels of Level 1: {result}")
    except ValueError:
        print("Please enter valid integers.")
if __name__ == "__main__":
    main()