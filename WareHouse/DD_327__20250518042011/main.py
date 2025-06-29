'''
Main application file for the Good Pair Checker.
'''
from typing import List
from good_pair import is_good_pair
def main():
    # Input reading
    try:
        input_data = input("Enter N, M, A, B (space-separated): ").strip().split()
        N = int(input_data[0])
        M = int(input_data[1])
        # Check if M is non-negative and does not exceed N
        if M < 0 or M > N:
            print("Error: M must be a non-negative integer and cannot exceed N.")
            return
        # Adjusted to read A and B based on M
        if M > 0:
            A = list(map(int, input_data[2:2 + M]))  # Read A from index 2 to 2 + M
            B = list(map(int, input_data[2 + M:2 + 2 * M]))  # Read B from index 2 + M to 2 + 2 * M
            # Validate that A and B contain valid indices and have the correct length
            if len(A) != M or len(B) != M:
                print("Error: A and B must have exactly M elements.")
                return
            if any(a < 1 or a > N for a in A) or any(b < 1 or b > N for b in B):
                print("Error: Values in A and B must be between 1 and N.")
                return
        else:
            A = []
            B = []
            print("No pairs to evaluate.")
            return 'Yes'  # No pairs to evaluate
        result = is_good_pair(N, M, A, B)
        print(result)
    except Exception as e:
        print("Error: " + str(e))
if __name__ == "__main__":
    main()