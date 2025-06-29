'''
Module containing the function to calculate the minimum time to reach stage N.
'''
from typing import List
def min_time_to_stage_n(N: int, A: List[int], B: List[int], X: List[int]) -> int:
    # Handle the case when N is 1
    if N == 1:
        return 0
    # Validate input parameters
    if N < 1 or len(A) != N - 1 or len(B) != N - 1 or len(X) != N - 1:
        raise ValueError("Invalid input: Ensure N is at least 1 and lists A, B, X are of length N-1.")
    for x in X:
        if x < 1 or x > N:
            raise ValueError("Invalid input: All elements in X must be between 1 and N.")
    # Initialize dp array with infinity
    dp = [float('inf')] * (N + 1)
    dp[1] = 0  # Starting point
    for i in range(1, N):
        # Calculate time to reach stage i+1
        new_time_to_next_stage = dp[i] + A[i - 1]
        dp[i + 1] = min(dp[i + 1], new_time_to_next_stage)
        # Calculate time to reach stage X[i-1] using teleportation
        if 1 <= X[i - 1] <= N:
            new_time_to_x_stage = dp[i] + B[i - 1]
            dp[X[i - 1]] = min(dp[X[i - 1]], new_time_to_x_stage)
    return dp[N]