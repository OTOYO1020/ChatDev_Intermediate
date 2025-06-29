'''
Main application file for the Score Game.
'''
from typing import List
from score_game import max_score
def main():
    '''
    Main function to run the Score Game application.
    '''
    N = int(input("Number of Squares (N): "))
    K = int(input("Maximum Moves (K): "))
    C = list(map(int, input("Scores on Squares (C) (comma-separated): ").split(',')))
    P = list(map(int, input("Permutation of Squares (P) (comma-separated): ").split(',')))
    # Convert P from 1-based to 0-based
    P = [p - 1 for p in P]
    # Validate permutation P
    if any(p < 0 or p >= N for p in P) or len(P) != len(set(P)):
        raise ValueError("Permutation P must contain unique values from 1 to N.")
    result = max_score(N, K, C, P)
    print(f"Maximum Score: {result}")
if __name__ == "__main__":
    main()