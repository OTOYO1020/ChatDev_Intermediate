'''
Main application file for the Sum Pairs Calculator.
'''
from calculator import calculate_sum_pairs
def main():
    try:
        # Read input from standard input
        N = int(input("Enter the number of integers (N): "))
        if N < 2 or N > 200000:
            raise ValueError("N must be between 2 and 200,000.")
        A = list(map(int, input("Enter integers (space-separated): ").split()))
        if len(A) != N:
            raise ValueError(f"Expected {N} integers, but got {len(A)}.")
        if any(x < 0 or x > 10**9 for x in A):
            raise ValueError("All elements must be between 0 and 10^9.")
        # Calculate the sum of products of pairs
        result = calculate_sum_pairs(N, A)
        print(f"Sum of products of pairs: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()