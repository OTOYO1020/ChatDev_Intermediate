'''
Module for calculating ball arrangements based on given conditions.
'''
mod = 10**9 + 7
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % mod
    return result
def count_valid_arrangements(N, M, K):
    valid_count = 0
    # Dynamic programming approach to count valid arrangements
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # Base case: one way to arrange 0 balls
    for n in range(N + 1):
        for m in range(M + 1):  # Iterate through all black balls
            if n > 0:
                # Ensure w_i ≤ b_i + K
                for b in range(max(0, n - K), m + 1):
                    dp[n][m] = (dp[n][m] + dp[n - 1][b]) % mod
            if m > 0:
                dp[n][m] = (dp[n][m] + dp[n][m - 1]) % mod
            if n > 0 and m > 0:
                dp[n][m] = (dp[n][m] + dp[n - 1][m - 1]) % mod
    valid_count = dp[N][M]
    return valid_count