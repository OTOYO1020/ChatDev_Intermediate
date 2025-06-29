'''
This module contains the function that encapsulates the logic for counting possible strings.
'''
def count_possible_strings(S: str, marked_chars: set) -> int:
    MODULO = 10**9 + 7
    marked_indices = [i for i, char in enumerate(S) if char in marked_chars]
    m = len(marked_indices)
    if m == 0:
        return 0
    dp = [0] * (m + 1)
    dp[0] = 1  # Base case: one way to form an empty string
    for i in range(1, m + 1):
        dp[i] = dp[i - 1]  # Not choosing the current marked character
        # Check if the current marked character can be chosen (not adjacent)
        if i > 1 and marked_indices[i - 1] - marked_indices[i - 2] > 1:
            dp[i] += dp[i - 1]  # Choosing the current marked character
        dp[i] += dp[i - 1]  # Also add the case where the previous marked character is not chosen
        dp[i] %= MODULO
    return (dp[m] - 1) % MODULO  # Subtract 1 to exclude the empty string