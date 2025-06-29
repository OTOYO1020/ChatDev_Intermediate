'''
Main application file for the Jump Reachability application.
'''
import sys
from jump_logic import canReach
def main():
    try:
        # Read N and X from standard input
        N, X = map(int, sys.stdin.readline().strip().split())
    except ValueError:
        print("Invalid input. Please enter two integers for N and X.")
        return
    jumps = []
    # Read the pairs of (a_i, b_i) for each jump
    for _ in range(N):
        try:
            a_i, b_i = map(int, sys.stdin.readline().strip().split())
            jumps.append((a_i, b_i))
        except ValueError:
            print("Invalid input. Please enter two integers for each jump.")
            return
    # Check if the target coordinate X can be reached
    if canReach(X, jumps):
        print("YES")
    else:
        print("NO")
if __name__ == "__main__":
    main()