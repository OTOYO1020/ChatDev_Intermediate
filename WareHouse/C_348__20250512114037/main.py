'''
Main entry point for the application to maximize minimum deliciousness.
'''
from typing import List
from utils import validate_input, maximize_min_deliciousness
def main():
    try:
        # Read input values
        N = int(input("Enter the number of bean types (N): "))
        A = list(map(int, input("Enter the deliciousness values (A) separated by commas: ").split(',')))
        C = list(map(int, input("Enter the colors (C) separated by commas: ").split(',')))
        # Validate input
        if validate_input(N, A, C):
            result = maximize_min_deliciousness(N, A, C)
            print(f"Max Min Deliciousness: {result}")
        else:
            print("Invalid input values. Please check the constraints.")
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()