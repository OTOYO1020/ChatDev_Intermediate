'''
Module to calculate the minimum cost to convert a binary string into a good string.
'''
from typing import List
def min_cost_to_good_string(S: str, C: List[int]) -> int:
    # Validate input string S
    if not (2 <= len(S) <= 200000) or any(c not in '01' for c in S):
        raise ValueError("String S must consist of '0' and '1' and have length 2 <= N <= 200000.")
    # Validate input list C
    if len(C) != len(S) or any(not (1 <= cost <= 10**9) for cost in C):
        raise ValueError("List C must have the same length as S and each cost must be in the range 1 <= C[i] <= 10^9.")
    # Check if the string is already a good string
    if all(S[i] == S[0] for i in range(len(S))):
        return 0  # No cost needed if the string is already good
    total_cost = 0
    n = len(S)
    i = 0
    while i < n - 1:
        if S[i] != S[i + 1]:
            # We have found a segment of differing characters
            cost_to_make_0 = 0
            cost_to_make_1 = 0
            # Count costs for the segment
            while i < n - 1 and S[i] != S[i + 1]:
                if S[i] == '0':
                    cost_to_make_1 += C[i]  # Cost to flip to '1'
                else:
                    cost_to_make_0 += C[i]  # Cost to flip to '0'
                i += 1
            # Include the last character of the segment
            if i < n:  # Ensure we are within bounds
                if S[i] == '0':
                    cost_to_make_1 += C[i]
                else:
                    cost_to_make_0 += C[i]
            # Add the minimum cost of this segment to the total cost
            total_cost += min(cost_to_make_0, cost_to_make_1)
        i += 1  # Move to the next character
    return total_cost