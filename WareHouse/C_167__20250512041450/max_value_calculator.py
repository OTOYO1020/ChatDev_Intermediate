'''
Module for calculating the maximum value based on input parameters.
'''
from typing import List
def calculate_max_value(N: int, M: int, X: int, C: List[int], A: List[List[int]]) -> int:
    # Validate input ranges
    if not (1 <= N <= 12) or not (1 <= M <= 12):
        raise ValueError("N and M must be in the range [1, 12].")
    if not (1 <= X <= 100000):
        raise ValueError("X must be in the range [1, 100000].")
    if any(not (1 <= c <= 100000) for c in C):
        raise ValueError("Each element in C must be in the range [1, 100000].")
    if any(any(not (0 <= a <= 100000) for a in row) for row in A):
        raise ValueError("Each element in A must be in the range [0, 100000].")
    # Initialize the dp array
    dp = [0] * (X + 1)  # dp[i] will hold the maximum value for budget i
    # Implementing a dynamic programming approach to solve the problem
    for i in range(N):
        cost = C[i]
        # Traverse backwards to avoid overwriting previous results
        for j in range(X, cost - 1, -1):
            for k in range(M):
                dp[j] = max(dp[j], dp[j - cost] + A[i][k])
    max_value = max(dp)  # The maximum value we can achieve with the budget X
    return max_value