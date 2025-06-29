'''
Main application file for the Majority Value Calculator.
'''
import sys
from utils import reduce_string, count_changes
def main():
    # Input handling
    binary_string = input("Enter binary string (length 3^N): ").strip()  # Trim whitespace
    n = input("Enter integer N: ").strip()  # Trim whitespace
    try:
        n = int(n)
        if len(binary_string) != 3 ** n or not all(c in '01' for c in binary_string):
            raise ValueError("Invalid input: The binary string must be of length 3^N and consist only of binary digits (0 or 1).")
        # Reduce the binary string
        reduced_value = reduce_string(binary_string, n)
        if len(reduced_value) != 1:
            raise ValueError("Reduced value must be a single character")
        # Determine the target value based on the reduced value
        target_value = '0' if reduced_value == '1' else '1'
        # Count changes needed
        changes_needed = count_changes(reduced_value, target_value)  # Compare reduced_value instead of original binary_string
        # Output the result
        print(f"Changes needed: {changes_needed}")
    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
if __name__ == "__main__":
    main()