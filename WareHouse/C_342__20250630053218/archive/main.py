'''
Main application file for the character replacement program.
'''
def main():
    # Read integer values N and Q
    N, Q = map(int, input().split())
    # Read the string S of length N
    S = input().strip()
    operations = []
    # Initialize a list to store Q pairs of characters (c_i, d_i)
    for _ in range(Q):
        c, d = input().split()
        operations.append((c, d))
    # Replace all occurrences of character c_i in string S with character d_i
    for c, d in operations:
        S = S.replace(c, d)
    # Print the modified string S as the output
    print(S)
if __name__ == "__main__":
    main()