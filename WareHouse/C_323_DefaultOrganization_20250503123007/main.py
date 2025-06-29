'''
Main entry point for the application that handles score calculations through standard input and output.
'''
from score_calculator import ScoreCalculator
if __name__ == "__main__":
    import sys
    # Read input
    N, M = map(int, sys.stdin.readline().strip().split())
    # Validate N and M
    if N <= 0 or M <= 0:
        raise ValueError("N and M must be positive integers.")
    A = list(map(int, sys.stdin.readline().strip().split()))
    # Validate scores length
    if len(A) != M:
        raise ValueError(f"The number of scores must match M. Expected {M}, got {len(A)}.")
    # Validate scores
    for score in A:
        if score < 500 or score > 2500 or score % 100 != 0:
            raise ValueError("Scores must be multiples of 100 and in the range of 500 to 2500.")
    S = [sys.stdin.readline().strip() for _ in range(N)]
    # Validate length of S
    if len(S) != N:
        raise ValueError("The number of solutions must match the number of players.")
    # Create an instance of ScoreCalculator
    score_calculator = ScoreCalculator(N, M, A, S)
    # Calculate results
    results = score_calculator.calculate_min_problems_to_solve()
    # Print results
    for result in results:
        print(result)