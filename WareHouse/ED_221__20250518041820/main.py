'''
Main application file for the subsequence calculator.
'''
import sys
from subsequence_calculator import count_valid_subsequences
def main():
    # Read input from standard input
    input_data = sys.stdin.read().strip().splitlines()
    N = int(input_data[0])
    A = list(map(int, input_data[1].split()))
    # Validate the length of the list A
    if len(A) != N:
        raise ValueError("The number of integers does not match N.")
    # Call the function to count valid subsequences
    result = count_valid_subsequences(N, A)
    # Output the result
    print(f"Valid Subsequences Count: {result}")
if __name__ == "__main__":
    main()