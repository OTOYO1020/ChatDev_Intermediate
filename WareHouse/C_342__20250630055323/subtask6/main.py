'''
Main application file for the String Replacer application.
'''
from utils import replace_characters_in_string
def main():
    # Read integer values N and Q from standard input
    N, Q = map(int, input().split())
    # Read the string S of length N from standard input
    S = input().strip()
    # Input validation for string length
    if len(S) != N:
        raise ValueError(f"The length of the string S must be {N}.")
    # Initialize a list to store Q pairs of characters (c_i, d_i) for the operations
    replacements = []
    # For each operation from 1 to Q
    for _ in range(Q):
        # Read the pair of characters (c_i, d_i) and store them in the list
        c, d = input().strip().split()
        replacements.append((c, d))
    # Replace all occurrences of character c_i in string S with character d_i
    modified_string = replace_characters_in_string(S, replacements)
    # Print the modified string S as the output
    print(modified_string)
if __name__ == "__main__":
    main()