'''
Utility functions for processing subsequences.
'''
from typing import List, Tuple
def max_11_22_subsequence(S: str, queries: List[Tuple[int, int]]) -> List[int]:
    results = []
    for L, R in queries:
        T = S[L-1:R]  # Adjust for 0-based indexing
        if len(T) == 0 or len(T) % 2 == 0:  # Check for empty or even length
            results.append(0)
            continue
        count_1 = T.count('1')
        count_2 = T.count('2')
        count_slash = T.count('/')
        # Calculate maximum length of valid subsequence
        if count_1 == 0 or count_2 == 0 or count_slash == 0:
            max_length = 0  # Set max_length to 0 if any count is zero
        else:
            # Calculate pairs of '1's and '2's that can be formed with '/'
            max_length = min(count_1, count_2) * 2  # Each pair contributes 2 to the length
            # Ensure that we do not exceed the number of '/' available
            max_length = min(max_length, count_slash)
        results.append(max_length)
    return results