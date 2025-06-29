'''
Main application file for the step reaching problem using standard input.
'''
import sys
from logic import can_reach_step
def main():
    try:
        # Read integers N, M, and X from standard input
        N, M, X = map(int, sys.stdin.readline().strip().split())
        if N < 0 or M < 0:
            print("Error: N and M must be non-negative integers.")
            return
    except ValueError:
        print("Error: Please enter valid integers for N, M, and X.")
        return
    # Read array A
    try:
        A = list(map(int, sys.stdin.readline().strip().split()))
        if len(A) != N:
            print("Error: The number of elements in A does not match N.")
            return
    except ValueError:
        print("Error: Please enter valid integers for the elements of A.")
        return
    # Read array B
    try:
        B = list(map(int, sys.stdin.readline().strip().split()))
        if len(B) != M:
            print("Error: The number of elements in B does not match M.")
            return
    except ValueError:
        print("Error: Please enter valid integers for the elements of B.")
        return
    # Call the function and print the result
    result = can_reach_step(N, M, A, B, X)  # Ensure X is passed correctly
    print(result)
if __name__ == "__main__":
    main()