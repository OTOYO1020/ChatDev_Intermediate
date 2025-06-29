'''
Module for calculating the minimum magic points needed to reduce monster health.
'''
from typing import List
def minimum_magic_points(H: int, N: int, A: List[int], B: List[int]) -> int:
    if H <= 0:
        return 0
    # Initialize a list to store the minimum magic points needed for each health value
    dp = [float('inf')] * (H + 1)
    dp[0] = 0  # No magic points needed to reduce health to 0
    # Iterate through each spell
    for i in range(N):
        spell_damage = A[i]
        spell_cost = B[i]
        # Update the dp array for each health value that can be reduced by this spell
        for j in range(spell_damage, H + 1):
            dp[j] = min(dp[j], dp[j - spell_damage] + spell_cost)
    return dp[H] if dp[H] != float('inf') else -1  # Return -1 if it's not possible to reduce health to 0