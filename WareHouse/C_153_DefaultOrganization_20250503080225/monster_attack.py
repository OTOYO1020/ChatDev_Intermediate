'''
Module for calculating the number of attacks needed to defeat monsters.
'''
def calculate_attacks(n, k, h):
    total_attacks = 0
    h.sort(reverse=True)  # Sort health in descending order
    for original_health in h:  # Iterate over the sorted health list
        health = original_health  # Use a temporary variable for health
        if health > 0 and k > 0:
            health -= 1  # Use a special move
            k -= 1
        # Calculate attacks needed to bring health to 0 only if health is greater than 0
        if health > 0:  # Corrected condition
            total_attacks += health  # Calculate attacks needed to bring health to 0
    return total_attacks