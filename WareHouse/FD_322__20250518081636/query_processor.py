'''
Module to process queries on a binary string.
'''
from typing import List, Tuple
def process_queries(S: str, queries: List[Tuple[int, int, int]]) -> List[int]:
    # Validate that the input string consists only of '0's and '1's
    if not S:  # Check for empty string
        raise ValueError("Input string cannot be empty.")
    if not all(c in '01' for c in S):
        raise ValueError("Input string must consist only of '0's and '1's.")
    results = []
    S = list(S)  # Convert string to list for mutability
    N = len(S)  # Store the length of S
    for c, L, R in queries:
        # Adjust for 0-based indexing
        L -= 1  
        R -= 1  
        # Validate indices after adjustment
        if L < 0 or R < 0 or L >= N or R >= N or L > R:
            raise ValueError(f"Invalid indices: L={L + 1}, R={R + 1} for string of length {N}.")
        if c == 1:
            flip_substring(S, L, R)
        elif c == 2:
            T = ''.join(S[L:R + 1])
            results.append(max_consecutive_ones(T))
    return results
def flip_substring(S: List[str], L: int, R: int):
    # Flip the characters in the substring from index L to R
    for i in range(L, R + 1):
        S[i] = '1' if S[i] == '0' else '0'
def max_consecutive_ones(T: str) -> int:
    # Calculate the maximum number of consecutive '1's in the string T
    max_count = 0
    current_count = 0
    for char in T:
        if char == '1':
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    return max_count