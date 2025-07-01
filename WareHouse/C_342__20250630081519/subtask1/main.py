'''
Main entry point for the character replacement application.
'''
from input_handler import InputHandler
from output_display import OutputDisplay
def main():
    # Read integer values N and Q
    N, Q = map(int, input().split())
    # Read the string S of length N
    S = input().strip()
    # Initialize a list to store Q pairs of characters (c_i, d_i)
    operations = []
    for _ in range(Q):
        c_i, d_i = input().split()
        operations.append((c_i.strip(), d_i.strip()))
    # Replace all occurrences of character c_i in string S with character d_i
    for c_i, d_i in operations:
        S = S.replace(c_i, d_i)
    # Print the modified string S as the output
    print(S)
if __name__ == "__main__":
    main()