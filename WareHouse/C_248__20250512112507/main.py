'''
Main application file for counting valid sequences based on user input.
'''
import sys
from sequence_counter import count_sequences
def main():
    try:
        # Prompt the user for input
        print("Please enter three integers N, M, and K (separated by spaces):")
        N, M, K = map(int, sys.stdin.read().strip().split())
        # Validate input constraints
        if not (1 <= N <= 50 and 1 <= M <= 50 and N <= K <= N * M):
            raise ValueError("Input values must satisfy: 1 ≤ N, M ≤ 50 and N ≤ K ≤ NM.")
        # Calculate the result
        result = count_sequences(N, M, K)
        # Print the result
        print(f"Valid Sequences Count: {result}")
    except ValueError as e:
        print(f"Input Error: {str(e)}")
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
if __name__ == "__main__":
    main()