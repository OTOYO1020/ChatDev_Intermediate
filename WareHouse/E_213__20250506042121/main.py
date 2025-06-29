'''
Main application file for the Takahashi Punches Calculator.
'''
import sys
from grid_utils import can_reach_market, min_punches_needed
def main():
    # Read integers H and W from standard input
    H, W = map(int, sys.stdin.readline().strip().split())
    # Read the grid representation S
    S = [sys.stdin.readline().strip() for _ in range(H)]
    # Calculate minimum punches needed
    min_punches = min_punches_needed(S, H, W)
    print(min_punches)
if __name__ == "__main__":
    main()