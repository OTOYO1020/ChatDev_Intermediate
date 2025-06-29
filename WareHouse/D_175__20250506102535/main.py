'''
Main entry point for the Score Calculator application.
'''
import sys
from score_calculator import calculate_score
def main():
    # Read integers N and K from standard input
    n, k = map(int, sys.stdin.readline().strip().split())
    # Read the array C of length N
    c = list(map(int, sys.stdin.readline().strip().split()))  # Changed to space-separated
    # Read the permutation array P of length N
    p = list(map(int, sys.stdin.readline().strip().split()))  # Changed to space-separated
    # Calculate the maximum score
    max_score = calculate_score(n, k, c, p)
    print(max_score)
if __name__ == "__main__":
    main()