'''
Main application file for the Snuke Cat Scarf Calculator.
'''
import sys
from scarf_calculator import restore_scarves
def main():
    '''
    Main function to handle input and output for the Snuke Cat Scarf Calculator.
    '''
    # Read input from standard input
    input_data = sys.stdin.read().strip().splitlines()
    try:
        N = int(input_data[0])
        # Validate input for N before reading the second line
        if N % 2 != 0 or N < 2 or N > 200000:
            print("Error: The value of N must be an even integer within the range [2, 200000]. Please check your input.")
            sys.exit(1)  # Exit the program immediately
        if len(input_data) < 2 or not input_data[1].strip():
            print("Error: The second line must contain space-separated integers.")
            sys.exit(1)  # Exit the program immediately
        # Read and validate the list of integers
        try:
            a = list(map(int, input_data[1].split()))
        except ValueError:
            print("Error: The second line must contain valid integers.")
            sys.exit(1)  # Exit the program immediately
        # Check if the length of 'a' matches 'N'
        if len(a) != N:
            print(f"Error: The number of XOR values must match N ({N}). Found {len(a)} values.")
            sys.exit(1)  # Exit the program immediately
        # Check if all values in 'a' are within the valid range
        if any(value < 0 or value > 10**9 for value in a):
            print("Error: One or more XOR values are out of the valid range (0 ≤ a[i] ≤ 10^9).")
            sys.exit(1)  # Exit the program immediately
    except ValueError:
        print("Error: Invalid input format. Please ensure the first line is an integer and the second line contains space-separated integers.")
        sys.exit(1)  # Exit the program immediately
    # Calculate scarf values
    try:
        scarf_values = restore_scarves(N, a)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)  # Exit the program immediately
    # Print the result as space-separated values
    print(' '.join(map(str, scarf_values)))
if __name__ == "__main__":
    main()