'''
Main application file for the contiguous ones calculator.
'''
import sys
from operations import min_operations_to_contiguous_ones
def main():
    # Read the binary string from standard input
    binary_string = input("Enter a binary string: ")
    try:
        result = min_operations_to_contiguous_ones(binary_string)
        print(f"Minimum operations: {result}")
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
if __name__ == "__main__":
    main()