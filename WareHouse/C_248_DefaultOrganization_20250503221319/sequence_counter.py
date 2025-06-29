'''
Module for counting valid integer sequences.
'''
def count_sequences(N, M, K):
    # Check if N is valid and M is at least 1
    if N <= 0 or M < 1:
        return 0
    # Check if K is less than N, if so, return 0 as no valid sequences can exist
    if K < N:
        print("No valid sequences can exist since K is less than N.")
        return 0
    # Create a DP table with (N+1) x (K+1) dimensions initialized to 0
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # Base case: one way to have a sequence of length 0 with sum 0
    # Fill the DP table
    for length in range(1, N + 1):
        for current_sum in range(K + 1):
            # Use cumulative sum to optimize the inner loop
            cumulative_sum = 0
            for x in range(1, M + 1):
                if current_sum >= x:
                    cumulative_sum += dp[length - 1][current_sum - x]
                    cumulative_sum %= 998244353
            dp[length][current_sum] = cumulative_sum
    # Sum all valid sequences of length N with sum <= K
    count = sum(dp[N][sum_value] for sum_value in range(K + 1)) % 998244353
    return count