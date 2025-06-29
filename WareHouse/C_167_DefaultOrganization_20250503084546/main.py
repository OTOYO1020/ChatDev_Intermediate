'''
Main application file for processing input and calculating the result.
'''
from calculator import calculate_result
def main():
    # Read integers N and M
    N, M = map(int, input().split())
    # Validate N and M
    if not (1 <= N <= 12 and 1 <= M <= 12):
        raise ValueError("N and M must be between 1 and 12 inclusive.")
    # Read integer X
    X = int(input())
    # Validate X
    if not (1 <= X <= 100000):
        raise ValueError("X must be between 1 and 100000 inclusive.")
    # Initialize list C and read M integers
    C = list(map(int, input().split()))
    # Validate C
    if len(C) != M or any(not (1 <= c <= 100000) for c in C):
        raise ValueError(f"C must contain exactly {M} integers, each between 1 and 100000 inclusive. Provided: {C}")
    # Initialize 2D list A and read N rows of M integers
    A = []
    for _ in range(N):
        row = list(map(int, input().split()))
        # Validate each row of A
        if len(row) != M or any(not (0 <= a <= 100000) for a in row):
            raise ValueError(f"Each row of A must contain exactly {M} integers, each between 0 and 100000 inclusive. Provided: {row}")
        A.append(row)
    # Calculate the result
    result = calculate_result(N, M, X, C, A)
    # Print the final value of result
    print(result)
if __name__ == "__main__":
    main()