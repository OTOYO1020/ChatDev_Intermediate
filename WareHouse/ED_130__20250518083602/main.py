'''
Main application file for counting subsequence pairs using standard input and output.
'''
import sys
from subsequence import count_subsequence_pairs
def main():
    # Read input from standard input
    input_data = sys.stdin.read().strip().splitlines()
    if len(input_data) < 2:
        print("Error: Please provide two sequences.")
        return
    # Parse sequences S and T
    try:
        S = list(map(int, input_data[0].strip().split()))  # Handle space-separated integers
        T = list(map(int, input_data[1].strip().split()))  # Handle space-separated integers
        # Validate lengths
        if not (1 <= len(S) <= 2000) or not (1 <= len(T) <= 2000):
            print("Error: Sequences must have lengths between 1 and 2000.")
            return
        # Count subsequence pairs
        result = count_subsequence_pairs(S, T)
        print(f"Total valid subsequence pairs: {result}")
    except ValueError:
        print("Error: Please enter valid integer sequences.")
if __name__ == "__main__":
    main()