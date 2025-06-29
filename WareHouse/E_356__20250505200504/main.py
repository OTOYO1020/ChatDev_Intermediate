'''
Main application file for the nested summation calculator using standard input and output.
'''
import sys
from calculator import calculate_sum
def main():
    # Read the length of the sequence
    N = int(sys.stdin.readline().strip())
    # Validate input for N
    if N < 2:
        print("Invalid input: N must be at least 2")
        return
    # Read the sequence of integers
    A = list(map(int, sys.stdin.readline().strip().split()))
    # Validate input
    if len(A) != N or any(x < 1 or x > 10**6 for x in A):
        print("Invalid input")
        return
    # Calculate the total sum
    total_sum = calculate_sum(N, A)
    # Print the result
    print(total_sum)
if __name__ == "__main__":
    main()