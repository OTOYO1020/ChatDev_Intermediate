'''
Module for counting valid subsequences based on given criteria.
'''
from typing import List
def count_valid_subsequences(N: int, A: List[int]) -> int:
    MOD = 998244353
    valid_pairs = 0
    # Count valid pairs (i, j) where A[i] <= A[j]
    for i in range(N):
        for j in range(i + 1, N):
            if A[i] <= A[j]:
                valid_pairs += 1
    # Calculate the number of valid subsequences of length at least 2
    count = 0
    if valid_pairs >= 2:
        # The number of ways to choose 2 pairs from valid_pairs
        count = (valid_pairs * (valid_pairs - 1) // 2) % MOD
        # Add combinations of length greater than 2
        # Each valid pair can be extended by choosing additional elements
        # that are greater than or equal to A[j] for the last element in the subsequence.
        for i in range(N):
            for j in range(i + 1, N):
                if A[i] <= A[j]:
                    # Count how many elements can be added to this pair
                    additional_count = sum(1 for k in range(j + 1, N) if A[j] <= A[k])
                    count = (count + additional_count) % MOD
    return count