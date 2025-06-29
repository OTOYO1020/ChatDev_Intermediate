'''
Main application file for the cost calculator.
'''
import sys
from cost_calculator import min_expected_cost
def main():
    try:
        # Read input from standard input with clearer instructions
        N, A, X, Y = map(int, input("Enter four integers N (N > 0), A (A > 0), X (X >= 0), Y (Y >= 0) separated by spaces: ").split())
        # Check constraints
        if N <= 0 or A <= 0 or X < 0 or Y < 0:
            raise ValueError("Invalid input values. Ensure N, A > 0 and X, Y >= 0.")
        cost = min_expected_cost(N, A, X, Y)
        print(f"Minimum Expected Cost: {cost:.2f}")
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()