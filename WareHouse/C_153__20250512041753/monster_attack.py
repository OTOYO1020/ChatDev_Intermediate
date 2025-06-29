'''
Module containing the function to calculate minimum attacks needed.
'''
from typing import List
def minimum_attacks(N: int, K: int, H: List[int]) -> int:
    if K == 0:
        return N  # If no special moves can be used, each monster requires one attack.
    # Sort healths in descending order
    H.sort(reverse=True)
    # Use special moves on the strongest monsters
    monsters_defeated = min(K, N)
    remaining_healths = H[monsters_defeated:]  # Remaining monsters after using special moves
    # If no remaining monsters, no attacks are needed
    if not remaining_healths:
        return 0
    # Total attacks needed to bring all remaining health to zero
    total_attacks_needed = 0
    for health in remaining_healths:
        total_attacks_needed += health  # Each monster requires 'health' attacks to be defeated
    return total_attacks_needed  # Return the total attacks needed