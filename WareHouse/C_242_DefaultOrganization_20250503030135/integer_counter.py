'''
Module to count valid integers based on specified rules using dynamic programming.
'''
class IntegerCounter:
    '''
    Class to implement the logic for counting valid integers.
    '''
    def count_valid_integers(self, n):
        '''
        Counts the valid integers of length N.
        '''
        modulo = 998244353
        # Initialize dp with an extra column for digit 0
        dp = [[0] * 10 for _ in range(n + 1)]
        # Base case: Initialize dp for length 1
        for j in range(1, 10):
            dp[1][j] = 1
        # Fill the dp array for lengths 2 to N
        for i in range(2, n + 1):
            for j in range(1, 10):  # Loop through digits from 1 to 9
                dp[i][j] = 0  # Initialize dp[i][j] to 0 before summing
                dp[i][j] += dp[i - 1][j - 1] if j > 1 else 0  # Only add if j-1 is valid
                dp[i][j] += dp[i - 1][j]  # Always include the middle digit
                dp[i][j] += dp[i - 1][j + 1] if j < 9 else 0  # Only add if j+1 is valid
                dp[i][j] %= modulo  # Apply modulo after addition
        # Calculate total valid integers of length N
        total_valid_integers = sum(dp[n][1:10]) % modulo  # Only include dp[n][1] to dp[n][9]
        return total_valid_integers