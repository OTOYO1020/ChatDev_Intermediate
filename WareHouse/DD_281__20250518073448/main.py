'''
Main entry point for the Greatest Multiple Application.
'''
import sys
from utils import greatest_multiple_of_D
def main():
    try:
        # Read input from standard input
        input_data = sys.stdin.read().strip().splitlines()
        # Validate input format
        if len(input_data) != 3:
            raise ValueError("Input must contain exactly three lines.")
        # Parse the list of integers A (allow whitespace-separated values)
        try:
            A = list(map(int, input_data[0].split()))
        except ValueError:
            raise ValueError("All elements in A must be valid integers.")
        # Validate that all elements in A are within the specified range
        if any(a < 0 or a > 10**9 for a in A):
            raise ValueError("All elements in A must be between 0 and 10^9.")
        # Parse K and D
        K = int(input_data[1])
        D = int(input_data[2])
        # Validate input constraints
        if not (1 <= K <= len(A) <= 100) or not (1 <= D <= 100):
            raise ValueError("Input constraints are not satisfied.")
        # Calculate the result
        result = greatest_multiple_of_D(A, K, D)
        print(f"Greatest multiple of {D}: {result}")
    except ValueError as ve:
        print(f"Input Error: {str(ve)}")
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
if __name__ == "__main__":
    main()