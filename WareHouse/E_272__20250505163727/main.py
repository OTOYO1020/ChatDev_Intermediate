'''
Main application file that initializes the application and handles user interactions.
'''
from utils import find_min_non_negative
def main():
    # Read integers N and M from standard input
    N, M = map(int, input().split())
    if N <= 0:
        print(0)  # If N is 0 or negative, the minimum non-negative integer is 0
        return
    # Read the integer sequence A of length N from standard input
    A = list(map(int, input().split()))
    # Validate the length of A
    if len(A) != N:
        print(f"Error: Expected {N} integers, but got {len(A)}.")
        return
    # Initialize a set 'A_set' to store the values of A for efficient lookup
    A_set = set(A)
    # Loop M times to perform the specified operation
    for _ in range(M):
        for i in range(1, N + 1):
            # Update the value of A[i] by adding i to it
            A[i - 1] += i  # Update A directly
            # Add the updated value to 'A_set'
            A_set.add(A[i - 1])  # Use the updated value directly
    # After updating all values, find the minimum non-negative integer not present in 'A_set'
    min_non_negative = find_min_non_negative(A_set)
    # Print the result of the minimum non-negative integer found after M operations
    print(min_non_negative)
if __name__ == "__main__":
    main()