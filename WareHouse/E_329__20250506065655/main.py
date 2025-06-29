'''
Main application file for the string matching functionality.
'''
from match_utils import can_match
def main():
    # Read lengths N and M, and strings S and T from standard input
    N = int(input("Enter length N: "))
    M = int(input("Enter length M: "))
    S = input("Enter string S: ")
    T = input("Enter string T: ")
    # Initialize X with '#' of length N
    X = '#' * N
    # Call the can_match function with the correct parameter order
    if can_match(X, S, T, N, M):
        print("YES")
    else:
        print("NO")
if __name__ == "__main__":
    main()