'''
Main file to run the Arithmetic Subsequence application.
'''
import sys
from arithmetic_subsequence import count_arithmetic_subsequences
def main():
    # Read input from standard input
    input_data = sys.stdin.read().strip().splitlines()
    N = int(input_data[0])
    A = list(map(int, input_data[1].split()))  # Changed to split() to handle space-separated integers
    # Calculate the counts of arithmetic subsequences
    result = count_arithmetic_subsequences(N, A)
    # Print the results in a structured format
    print("Counts of Arithmetic Subsequences:")
    for k in range(1, N + 1):
        print(f"Length {k}: {result[k - 1]}")
if __name__ == "__main__":
    main()