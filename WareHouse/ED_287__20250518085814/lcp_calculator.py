'''
Module for calculating the longest common prefix (LCP) between strings.
'''
from typing import List
def lcp(x: str, y: str) -> int:
    '''
    Calculate the longest common prefix between two strings.
    '''
    min_length = min(len(x), len(y))
    for i in range(min_length):
        if x[i] != y[i]:
            return i
    return min_length
def max_lcp(strings: List[str]) -> List[int]:
    '''
    Calculate the maximum LCP for each string against all other strings.
    This implementation sorts the strings and compares adjacent strings.
    '''
    n = len(strings)
    max_lcp_values = [0] * n
    # Pair strings with their original indices for result mapping
    indexed_strings = list(enumerate(strings))
    indexed_strings.sort(key=lambda x: x[1])  # Sort by string value
    # Compare adjacent strings in the sorted order
    for i in range(n - 1):
        idx1, str1 = indexed_strings[i]
        idx2, str2 = indexed_strings[i + 1]
        lcp_value = lcp(str1, str2)
        max_lcp_values[idx1] = max(max_lcp_values[idx1], lcp_value)
        max_lcp_values[idx2] = max(max_lcp_values[idx2], lcp_value)
    return max_lcp_values