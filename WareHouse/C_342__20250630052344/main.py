'''
Main application file for the character replacement tool.
'''
def main():
    # Read the integer values N and Q from standard input
    N, Q = map(int, input().split())
    # Validate N and Q
    if N < 0 or Q < 0:
        print("N and Q must be non-negative integers.")
        return
    # Read the string S of length N from standard input
    S = input().strip()
    # Validate the length of S
    if len(S) != N:
        print(f"The length of S must be {N}.")
        return
    # Initialize a list to store Q pairs of characters (c_i, d_i) for the operations
    replacements = []
    # For each operation from 1 to Q
    for _ in range(Q):
        # Read the pair of characters (c_i, d_i) and store them in the list
        c, d = input().strip().split()
        # Validate that c and d are single characters
        if len(c) != 1 or len(d) != 1:
            print("Each character pair must consist of exactly two characters.")
            return
        replacements.append((c, d))
    # For each operation in the list of pairs
    for c, d in replacements:
        # Replace all occurrences of character c_i in string S with character d_i
        S = S.replace(c, d)
    # After all operations are completed, print the modified string S as the output
    print(S)
if __name__ == "__main__":
    main()