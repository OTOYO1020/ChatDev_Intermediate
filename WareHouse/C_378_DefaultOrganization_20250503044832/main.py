'''
Main application file for the recent positions finder.
'''
from utils import find_recent_positions
def main():
    # Read the integer N from standard input, which indicates the length of the sequence
    N = int(input())
    # Validate input: Ensure N is a positive integer
    if N <= 0:
        print("Error: N must be a positive integer.")
        return
    # Read the sequence of positive integers A from standard input and convert it to a list of integers
    A = list(map(int, input().split()))
    # Validate input: Ensure the length of the sequence matches N and all numbers are positive integers
    if len(A) != N or any(num <= 0 for num in A):
        print("Error: Please ensure the length of the sequence matches N and all numbers are positive integers.")
        return
    # Find recent positions of each number in the sequence
    positions = find_recent_positions(N, A)
    # Print the output in the specified format as space-separated integers
    print(" ".join(map(str, positions)))
if __name__ == "__main__":
    main()