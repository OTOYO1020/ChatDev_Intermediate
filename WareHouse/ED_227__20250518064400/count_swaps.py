'''
Module to count the number of valid strings that can be formed with a given number of adjacent swaps.
'''
from math import factorial
from collections import Counter
def count_swaps(S: str, K: int) -> int:
    # Validate the length of the string
    if not (2 <= len(S) <= 30):
        raise ValueError("String length must be between 2 and 30 characters.")
    # Validate the value of K
    if not (0 <= K <= 10**9):
        raise ValueError("K must be a non-negative integer and cannot exceed 10^9.")
    # Count occurrences of each character
    count = Counter(S)
    # Calculate the number of unique permutations
    total_permutations = factorial(len(S))
    for char in count:
        total_permutations //= factorial(count[char])
    # Calculate the maximum number of adjacent swaps possible
    max_swaps = sum(count.values()) - 1  # Maximum adjacent swaps possible
    # If K is greater than or equal to max_swaps, all permutations are valid
    if K >= max_swaps:
        return total_permutations
    # Calculate valid arrangements based on character counts and allowed swaps
    valid_strings = count_valid_permutations(count, K)
    return valid_strings
def count_valid_permutations(count, K: int) -> int:
    '''
    Calculate valid arrangements based on character counts and allowed swaps K.
    This function uses combinatorial logic to count valid arrangements without generating all permutations.
    '''
    total_valid = 0
    n = sum(count.values())  # Total number of characters
    # Generate a sorted list of characters based on their counts
    char_list = []
    for char, cnt in count.items():
        char_list.extend([char] * cnt)
    # Use a dynamic programming approach to count valid arrangements
    dp = [[0] * (K + 1) for _ in range(n + 1)]
    dp[0][0] = 1  # Base case: one way to arrange zero characters with zero swaps
    for i in range(1, n + 1):
        for j in range(K + 1):
            dp[i][j] = dp[i - 1][j]  # Not using the current character
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1] * (i - 1)  # Using the current character with a swap
    total_valid = sum(dp[n][j] for j in range(K + 1))
    return total_valid