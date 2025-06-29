'''
Main application file for the valid divisions counter.
'''
import sys
from division_counter import count_divisions
def main():
    # Read input from standard input
    input_data = sys.stdin.read().strip().splitlines()
    N, K = map(int, input_data[0].split())
    A = list(map(int, input_data[1].split()))
    if len(A) != N:
        raise ValueError("Length of sequence A must be equal to N.")
    # Call the function to count valid divisions and print the result
    result = count_divisions(A, K)
    print(result)  # Output the result as per the task requirement
if __name__ == "__main__":
    main()