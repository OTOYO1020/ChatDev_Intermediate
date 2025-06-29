'''
Module for calculating the number of ways to reach cell N based on segments.
'''
def calculate_ways(N, K, segments):
    if N < 1 or K < 1:
        return 0  # No ways to reach cell N if N < 1 or no segments are provided
    MOD = 998244353
    S = set()
    # Construct the set S from the segments
    for segment in segments:
        if len(segment) != 2:
            raise ValueError("Each segment must contain exactly two integers (L_i and R_i).")
        L, R = segment
        if L > R:
            raise ValueError(f"Invalid segment: L ({L}) cannot be greater than R ({R}).")
        # Add all integers from L to R to the set S
        S.update(range(L, R + 1))  # Include all integers in the segment
    if not S:  # If S is empty, no valid segments exist
        return 0
    # Initialize ways list
    ways = [0] * (N + 1)
    ways[1] = 1  # Starting position
    # Loop through each cell i from 1 to N
    for i in range(1, N + 1):
        for d in S:
            if i + d <= N:
                ways[i + d] = (ways[i + d] + ways[i]) % MOD
    return ways[N]