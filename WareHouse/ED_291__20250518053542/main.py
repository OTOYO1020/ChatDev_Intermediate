'''
Main application file for the permutation checker.
'''
import sys
import re
from permutation import can_determine_permutation
def main():
    try:
        N = int(input("Enter N (length of sequence): "))
        M = int(input("Enter M (number of pairs): "))
        pairs_input = input("Enter pairs (e.g., '(1, 2) (2, 3)'): ")
        # Validate pairs input
        pairs = []
        # Use regex to find pairs in the format (X, Y)
        matches = re.findall(r'\(\s*(\d+)\s*,\s*(\d+)\s*\)', pairs_input)
        for match in matches:
            x, y = map(int, match)
            if 1 <= x <= N and 1 <= y <= N:
                pairs.append((x, y))
            else:
                raise ValueError("Pairs must be within the range of 1 to N.")
        can_determine, permutation = can_determine_permutation(N, M, pairs)
        if can_determine:
            print(f"Unique permutation found: {permutation}")
        else:
            print("No unique permutation can be determined.")
    except Exception as e:
        print(f"Input Error: {str(e)}", file=sys.stderr)
if __name__ == "__main__":
    main()