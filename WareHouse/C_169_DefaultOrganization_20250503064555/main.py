'''
Main application file for the truncated product calculator.
'''
import sys
import re
from computation import compute_truncated_product
def main():
    try:
        A = int(input("Enter an integer (A): "))
        B_input = input("Enter a floating-point number (B) with two decimal places or in scientific notation: ")
        # Validate B_input to ensure it has exactly two decimal places or is in scientific notation
        if not re.match(r'^-?\d+\.\d{2}$|^-?\d+(\.\d{2})?[eE][-+]?\d+$', B_input):
            raise ValueError("B must be a floating-point number with exactly two digits after the decimal point or in scientific notation.")
        B = float(B_input)
        result = compute_truncated_product(A, B)
        print(result)  # Print the result as a single integer
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()