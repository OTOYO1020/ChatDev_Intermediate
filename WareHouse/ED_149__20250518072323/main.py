'''
Main application file for the Happiness Calculator.
'''
from typing import List  # Added import for clarity
import sys
from happiness_calculator import max_happiness
def main():
    try:
        N = int(input("Enter the number of guests (N): "))
        M = int(input("Enter the number of handshakes (M): "))
        A = list(map(int, input("Enter the powers of guests (comma-separated integers): ").split(',')))  # Updated prompt
        if len(A) != N:
            raise ValueError("The number of powers must match the number of guests.")
        happiness = max_happiness(N, M, A)
        print(f"Maximum Happiness: {happiness}")
    except Exception as e:
        print(f"Input Error: {e}", file=sys.stderr)
if __name__ == "__main__":
    main()