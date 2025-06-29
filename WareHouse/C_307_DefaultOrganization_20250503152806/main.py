'''
Main application file for the sheet overlay and cut-out checker.
'''
import sys
from sheet import create_sheet_C, can_cut_out
def main():
    # Read dimensions from standard input
    H_A, W_A, H_B, W_B, H_X, W_X = map(int, sys.stdin.readline().strip().split())
    # Validate dimensions before reading sheets
    if H_A < 0 or W_A < 0 or H_B < 0 or W_B < 0 or H_X < 0 or W_X < 0:
        print("Invalid dimensions provided.")
        return
    # Read sheets A, B, and X
    A = [sys.stdin.readline().strip() for _ in range(H_A)]
    B = [sys.stdin.readline().strip() for _ in range(H_B)]
    X = [sys.stdin.readline().strip() for _ in range(H_X)]
    # Create sheet C
    C = create_sheet_C(A, B)
    # Check if cut-out can be achieved
    result = can_cut_out(C, X, H_X, W_X, A, B)
    # Print result
    if result:
        print("YES")
    else:
        print("NO")
if __name__ == "__main__":
    main()