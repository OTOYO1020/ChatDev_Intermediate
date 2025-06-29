'''
Logic for calculating the number of ways to reach cell N.
'''
from typing import List, Tuple
def countWays(N: int, K: int, segments: List[Tuple[int, int]]) -> int:
    MOD = 998244353
    # Merge overlapping and adjacent segments
    segments.sort()  # Sort segments by their starting point
    merged_segments = []
    for seg in segments:
        if not merged_segments or merged_segments[-1][1] < seg[0] - 1:  # Allow adjacency
            merged_segments.append(list(seg))  # Convert tuple to list for mutability
        else:
            # Update the last segment's end to the maximum end of the overlapping segments
            merged_segments[-1][1] = max(merged_segments[-1][1], seg[1])
    # Check if Cell 1 is covered by any segment or if we can reach it indirectly
    reachable = False
    for L, R in merged_segments:
        if L <= 1 <= R:
            reachable = True
            break
        if L <= 1:
            reachable = True  # We can reach Cell 1 indirectly
    if not reachable:
        return 0  # No way to start from Cell 1
    # Create the set S from merged segments
    S = set()
    for L, R in merged_segments:
        S.update(range(L, R + 1))
    # Check if N is less than the minimum L in the segments
    min_L = min(seg[0] for seg in merged_segments)
    if N < min_L:
        return 0  # No way to reach Cell N
    # Check if Cell N is covered by any segment
    if not any(L <= N <= R for L, R in merged_segments):
        return 0  # No way to reach Cell N
    ways = [0] * (N + 1)
    ways[1] = 1  # Starting point
    for i in range(1, N + 1):
        for d in S:
            if i + d <= N:
                ways[i + d] = (ways[i + d] + ways[i]) % MOD
    return ways[N]