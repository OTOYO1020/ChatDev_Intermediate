'''
Main entry point for the application that handles user interactions.
'''
import sys
from utils import count_numbers_with_n_divisors
def main():
    try:
        N = int(input("Enter a number (N): "))
        if N < 1:
            raise ValueError("N must be a positive integer.")
        count = count_numbers_with_n_divisors(N, 9)
        print(f"Count of numbers with exactly 9 divisors: {count}")
    except ValueError as e:
        print(f"Input Error: {str(e)}", file=sys.stderr)
if __name__ == "__main__":
    main()