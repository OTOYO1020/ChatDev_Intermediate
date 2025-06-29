'''
Utility class to calculate the total number of valid strings based on input constraints.
'''
class StringCalculator:
    MOD = 998244353
    def __init__(self, k, c):
        self.k = k
        self.c = c
    def count_valid_strings(self):
        total_count = 0
        for length in range(1, self.k + 1):
            total_count += self.calculate_for_length(length)
            total_count %= self.MOD
        return total_count
    def calculate_for_length(self, length):
        # dp[i][j] will store the number of ways to form a string of length j using the first i letters
        dp = [[0] * (length + 1) for _ in range(27)]
        dp[0][0] = 1  # Base case: one way to form an empty string with 0 letters
        for letter_index in range(1, 27):
            max_count = self.c[letter_index - 1]
            for current_length in range(length + 1):
                # Start with the case of not using the current letter
                dp[letter_index][current_length] = dp[letter_index - 1][current_length]
                # Iterate over the possible counts of the current letter
                for count in range(1, min(max_count, current_length) + 1):
                    dp[letter_index][current_length] += dp[letter_index - 1][current_length - count]
                    dp[letter_index][current_length] %= self.MOD
            # Cumulative sum for the current letter
            for current_length in range(1, length + 1):
                dp[letter_index][current_length] += dp[letter_index][current_length - 1]
                dp[letter_index][current_length] %= self.MOD
        return dp[26][length]  # Return the number of ways to form the string of the specified length