'''
Module to count valid strings based on given constraints.
'''
from typing import List
def count_valid_strings(K: int, C: List[int]) -> int:
    MOD = 998244353
    total_valid_strings = 0
    total_letters = sum(1 for occurrences in C if occurrences > 0)
    # If there are no valid letters, return 0 as only empty strings are valid
    if total_letters == 0:
        return 0
    # Calculate the total occurrences of letters
    total_occurrences = sum(C)
    # Adjust K if it exceeds the total occurrences
    if K > total_occurrences:
        K = total_occurrences  # Limit K to the maximum possible length of valid strings
    for length in range(1, K + 1):
        valid_count = 1  # Start with 1 for the empty product
        for i in range(26):
            if C[i] > 0:
                # Calculate the number of valid occurrences for this letter
                valid_count *= (min(C[i], length) + 1)  # +1 to include the option of not using the letter
                valid_count %= MOD
        # The valid_count now represents the total combinations for the current length
        valid_count = (valid_count - 1 + MOD) % MOD  # Exclude empty string option
        total_valid_strings += valid_count
        total_valid_strings %= MOD
    return total_valid_strings