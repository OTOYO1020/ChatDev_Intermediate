'''
Main application file for the String Modifier.
'''
from string_modifier import replace_characters
def main():
    # Read integer values N and Q from standard input
    N, Q = map(int, input().split())
    # Read the string S of length N from standard input
    S = input().strip()
    # Initialize a list to store Q pairs of characters (c_i, d_i)
    pairs = []
    for _ in range(Q):
        # Read the pair of characters (c_i, d_i) and store them in the list
        c_i, d_i = input().strip().split()
        pairs.append((c_i, d_i))
    # Replace characters in the string S based on the provided pairs
    modified_string = replace_characters(S, pairs)
    # Print the modified string S as the output
    print(modified_string)
if __name__ == "__main__":
    main()