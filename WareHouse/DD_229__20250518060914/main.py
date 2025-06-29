'''
Main application file for the Max Consecutive Xs application.
'''
import sys
from max_consecutive_xs import max_consecutive_Xs
def main():
    # Read input from standard input
    input_data = sys.stdin.read().strip().splitlines()
    # Validate input for S
    if len(input_data) < 1 or not input_data[0]:
        print("Input Error: S must be a non-empty string.")
        return
    S = input_data[0]
    # Validate that S contains at least one 'X' or '.'
    if not any(char in 'X.' for char in S):
        print("Input Error: S must contain at least one 'X' or '.' character.")
        return
    # Validate input for K
    if len(input_data) < 2:
        print("Input Error: K must be provided.")
        return
    try:
        K = int(input_data[1])
    except ValueError:
        print("Input Error: K must be an integer between 0 and 200,000.")
        return
    # Validate input ranges
    if not (1 <= len(S) <= 200000) or not (0 <= K <= 200000):
        print("Input Error: Invalid input values. Ensure the length of S is between 1 and 200,000 and K is between 0 and 200,000.")
        return
    # Check if S consists entirely of '.' characters
    if all(char == '.' for char in S):
        print(K)  # Directly output K since we can convert all '.' to 'X'
        return
    # Calculate the maximum consecutive Xs
    max_count = max_consecutive_Xs(S, K)
    print(max_count)
if __name__ == "__main__":
    main()