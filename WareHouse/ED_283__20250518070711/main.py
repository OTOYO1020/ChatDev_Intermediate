'''
Main application file for the Matrix Isolation software.
'''
import sys
from typing import List, Tuple
from matrix_operations import min_operations_to_isolate
def main():
    # Read matrix dimensions from standard input
    try:
        H, W = map(int, input("Enter matrix dimensions (H W): ").strip().split())
        if H <= 0 or W <= 0:
            raise ValueError("Matrix dimensions must be positive integers.")
        A = []
        print("Enter the matrix rows (space-separated values):")
        for _ in range(H):
            row = list(map(int, input().strip().split()))
            if len(row) != W:
                raise ValueError("Matrix dimensions do not match the input.")
            A.append(row)
        possible, operations = min_operations_to_isolate(H, W, A)
        result_text = f"Possible: {possible}, Operations: {operations}"
        print(result_text)
    except Exception as e:
        print(f"Input Error: {e}", file=sys.stderr)
if __name__ == "__main__":
    main()