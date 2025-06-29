'''
Main application file for the Max Value Calculator.
'''
import sys
from max_value_calculator import calculate_max_value
def main():
    try:
        N = int(input("Enter N (1-12): "))
        M = int(input("Enter M (1-12): "))
        X = int(input("Enter X (1-100000): "))
        C_input = input("Enter C (comma-separated values, 1-100000): ")
        C = list(map(int, C_input.split(',')))
        A_input = input("Enter A (2D list as semicolon-separated rows of comma-separated values): ")
        A = [list(map(int, row.split(','))) for row in A_input.split(';')]
        # Validate lengths of C and A
        if len(C) != N:
            raise ValueError(f"The length of C must be {N}.")
        if len(A) != N:
            raise ValueError(f"A must be a 2D list with {N} rows.")
        if any(len(row) != M for row in A):
            raise ValueError(f"Each row in A must have {M} columns.")
        # Validate each element in C
        if any(not (1 <= c <= 100000) for c in C):
            raise ValueError("Each element in C must be in the range [1, 100000].")
        # Validate each element in A
        if any(any(not (0 <= a <= 100000) for a in row) for row in A):
            raise ValueError("Each element in A must be in the range [0, 100000].")
        # Check for empty lists
        if not C:
            raise ValueError("C cannot be an empty list.")
        if not A or any(not row for row in A):
            raise ValueError("A cannot be an empty 2D list and must contain valid rows.")
        max_value = calculate_max_value(N, M, X, C, A)
        print(f"Max Value: {max_value}")
    except ValueError as ve:
        print(f"Input Error: {ve}. Please ensure you follow the input format.", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)
if __name__ == "__main__":
    main()