'''
Module for counting the number of ways to choose characters from a string.
'''
MOD = 10**9 + 7
target = ['c', 'h', 'o', 'k', 'u', 'd', 'a', 'i']
def count_ways(S: str) -> int:
    # Check if the input string is shorter than the target sequence
    if len(S) < len(target):
        return 0
    # Initialize a dynamic programming array to store counts of ways
    dp = [0] * (len(target) + 1)
    dp[0] = 1  # Base case: one way to choose an empty sequence
    # Iterate through each character in the input string
    for char in S:
        # Update the dp array in reverse order to avoid overwriting
        for j in range(len(target) - 1, -1, -1):
            if char == target[j]:
                # If the character matches the target, update the count of ways
                dp[j + 1] = (dp[j + 1] + dp[j]) % MOD
    # Return the number of ways to form the complete target sequence
    return dp[len(target)]