'''
Main application file for calculating the N-th smallest sum of three repunits.
'''
import sys
from repunit_generator import RepunitGenerator
def main():
    try:
        n = int(input("Please enter an integer N (between 1 and 333 inclusive): "))
        if n < 1 or n > 333:
            raise ValueError("N must be between 1 and 333.")
        generator = RepunitGenerator()
        result = generator.calculate_unique_sums(n, limit=333)  # Set limit to 333
        print(result)  # Print only the result as a single integer
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()