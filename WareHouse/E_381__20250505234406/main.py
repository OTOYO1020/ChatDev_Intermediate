'''
Main application file for the subsequence length calculator.
'''
import sys
from subsequence_calculator import SubsequenceCalculator
def main():
    # Read integers N and Q from standard input
    N, Q = map(int, sys.stdin.readline().strip().split())
    # Input validation for N and Q
    if N <= 0 or Q <= 0:
        print("N and Q must be positive integers.")
        return
    # Read the string S
    S = sys.stdin.readline().strip()
    # Validate the length of S
    if len(S) != N:
        print(f"Error: The length of the string S must be exactly {N}.")
        return
    # Read the queries
    queries = []
    for _ in range(Q):
        L, R = map(int, sys.stdin.readline().strip().split())
        queries.append((L, R))
    # Create an instance of SubsequenceCalculator
    calculator = SubsequenceCalculator(S)
    max_length = calculator.max_valid_subsequence_length(queries)
    # Print the maximum length of the valid 11/22 subsequence found
    print(max_length)
if __name__ == "__main__":
    main()