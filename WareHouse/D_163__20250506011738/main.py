'''
Main application file for the unique sums calculator.
'''
from sum_calculator import SumCalculator
import sys
def main():
    # Read integers N and K from standard input
    try:
        N, K = map(int, sys.stdin.readline().strip().split())
        if N < 0 or K < 0:
            print("N and K must be non-negative integers.")
            return
        if N > 100:  # Limit N to a maximum of 100 for performance reasons
            print("N is too large. Please enter a value less than or equal to 100.")
            return
    except ValueError:
        print("Invalid input. Please enter two integers.")
        return
    # Initialize the calculator and calculate unique sums
    calculator = SumCalculator(N, K)
    result = calculator.calculate_unique_sums()
    # Display the result
    if isinstance(result, str):  # Check if the result is a message
        print(result)
    else:
        print(f"Unique Sums Count: {result}")
if __name__ == "__main__":
    main()