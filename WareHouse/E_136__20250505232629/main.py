'''
Main application file for the GCD and Max Divisor Calculator.
'''
import sys
from gcd_calculator import calculate_gcd, calculate_max_divisor
def main():
    try:
        # Read inputs from standard input
        n = int(input())
        if n <= 0:
            raise ValueError("N must be a positive integer.")
        k = int(input())
        if k < 0:
            raise ValueError("K must be a non-negative integer.")
        a = list(map(int, input().split()))
        if len(a) != n:
            raise ValueError("Number of elements does not match N.")
        # Validate that all elements are positive integers
        if any(x <= 0 for x in a):
            raise ValueError("All elements must be positive integers.")
        # Calculate the maximum divisor
        max_divisor = calculate_max_divisor(a, k)
        print(max_divisor)
    except Exception as e:
        print(f"Input Error: {str(e)}", file=sys.stderr)
if __name__ == "__main__":
    main()