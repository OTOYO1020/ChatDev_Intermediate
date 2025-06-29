'''
Main application file for the Weight Difference Calculator.
'''
import sys
from weight_difference import calculate_min_difference
def main():
    try:
        n = int(input("Enter the number of weights (N): "))  # Clarified input prompt
        if n < 2:
            print("Error: At least two weights are required for a valid division.", file=sys.stderr)
            return  # Exit the function early
        try:
            weights = list(map(int, input("Enter the weights separated by spaces (indexed from 1 to N): ").split()))
        except ValueError:
            print("Error: All weights must be integers.", file=sys.stderr)
            return  # Exit the function early
        if len(weights) != n:
            raise ValueError("Number of weights does not match N.")
        # Check for non-negative weights
        if any(w < 0 for w in weights):
            raise ValueError("Weights must be non-negative.")
        min_difference = calculate_min_difference(weights)
        print(min_difference)
    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
if __name__ == "__main__":
    main()