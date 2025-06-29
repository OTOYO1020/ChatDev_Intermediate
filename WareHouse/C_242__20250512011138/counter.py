'''
Module for counting valid integers based on the input N.
'''
def count_valid_integers(N: int) -> int:
    mod = 998244353
    # Initialize the dynamic programming table with 10 columns for digits 0 to 9
    dp = [[0] * 10 for _ in range(N + 1)]  # 10 columns for digits 0 to 9, but we will only use 1-9
    # Base case: single-digit integers (1 to 9)
    for j in range(1, 10):
        dp[1][j] = 1  # Store in dp[1][1] to dp[1][9]
    # Fill the dp table for lengths from 2 to N
    for i in range(2, N + 1):
        for j in range(1, 10):  # j should be from 1 to 9
            dp[i][j] = 0  # Initialize dp[i][j] to 0 before accumulation
            for k in range(1, 10):  # k should also be from 1 to 9
                if abs(j - k) >= 2:  # Ensure the digit difference condition is met
                    dp[i][j] = (dp[i][j] + dp[i - 1][k]) % mod  # Accumulate counts correctly
    # Sum up valid integers of length N (only considering digits 1 to 9)
    total_count = sum(dp[N][j] for j in range(1, 10)) % mod
    return total_count