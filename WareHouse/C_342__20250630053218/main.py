'''
Main application file for the character replacement program.
'''
def main():
    try:
        # Read integer values N and Q
        N, Q = map(int, input().split())
        if N <= 0 or Q < 0:
            print("Error: N must be a positive integer and Q must be a non-negative integer.")
            return
    except ValueError:
        print("Error: Please enter valid integers for N and Q.")
        return
    # Read the string S of length N
    S = input().strip()
    # Validate that the length of S matches N
    if len(S) != N:
        print(f"Error: The length of the string S must be {N}. Received length: {len(S)}")
        return
    # Initialize a list to store Q pairs of characters (c_i, d_i)
    replacements = []
    # Read Q pairs of characters
    for _ in range(Q):
        c, d = input().split()
        # Validate that both c and d are single characters
        if len(c) != 1 or len(d) != 1:
            print(f"Error: Both characters must be single characters. Received: '{c}', '{d}'")
            return
        replacements.append((c, d))  # Store the replacement in a list
    # Apply replacements one by one to avoid cascading effects
    for c, d in replacements:
        S = S.replace(c, d)
    # Print the modified string S as the output
    print(S)
if __name__ == "__main__":
    main()