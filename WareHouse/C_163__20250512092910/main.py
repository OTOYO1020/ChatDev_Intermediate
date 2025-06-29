'''
Main application file for the Subordinate Counter.
'''
from subordinate_counter import count_subordinates
def main():
    # Read input from standard input
    N = int(input())
    A = list(map(int, input().split()))
    # Validate the length of A
    if len(A) != N - 1:
        raise ValueError("Length of A must be N-1.")
    # Calculate subordinate counts
    results = count_subordinates(N, A)
    # Print the results as a space-separated string
    print(" ".join(map(str, results)))
if __name__ == "__main__":
    main()