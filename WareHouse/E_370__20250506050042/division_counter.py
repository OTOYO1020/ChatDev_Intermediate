'''
Module for counting valid divisions of a sequence.
'''
from typing import List
def count_divisions(A: List[int], K: int) -> int:
    N = len(A)
    count_valid_divisions = 0
    MOD = 998244353
    # Create a prefix sum array for efficient sum calculations
    prefix_sum = [0] * (N + 1)
    for i in range(N):
        prefix_sum[i + 1] = prefix_sum[i] + A[i]
    def is_valid_partition(indices: List[int]) -> bool:
        # Check all subsequences defined by the indices
        for i in range(len(indices) - 1):
            current_sum = prefix_sum[indices[i + 1]] - prefix_sum[indices[i]]
            if current_sum == K:
                return False  # Found a subsequence that sums to K
        # Check the last subsequence
        if indices[-1] != N:  # Ensure we are within bounds
            current_sum = prefix_sum[N] - prefix_sum[indices[-1]]  # From the last index to the end of A
            if current_sum == K:
                return False  # Last subsequence sums to K
        return True  # No subsequence sums to K
    def generate_partitions(start: int, indices: List[int]):
        nonlocal count_valid_divisions
        if start >= N:
            if is_valid_partition(indices):
                count_valid_divisions += 1
            return
        for end in range(start + 1, N + 1):  # end should be start + 1 to N
            generate_partitions(end, indices + [start])  # Use 'start' to ensure continuity
    generate_partitions(0, [])
    return count_valid_divisions % MOD