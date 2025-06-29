'''
Utility functions for generating combinations of switch states and validating bulbs.
'''
from itertools import product
def generate_combinations(n):
    '''Generate all possible combinations of switch states for N switches.'''
    return product([False, True], repeat=n)  # Return combinations as a generator
def validate_bulbs(combination, bulbs):
    '''Check if the current combination satisfies the bulbs' requirements.'''
    for bulb in bulbs:
        if len(bulb.connected_switches) == 0:
            # If there are no connected switches, the bulb is satisfied regardless of its required parity
            continue
        on_count = sum(1 for index in bulb.connected_switches if 1 <= index <= len(combination) and combination[index - 1])  # Ensure index is valid
        # Corrected logic to ensure we are checking the correct indices
        if on_count % 2 != bulb.required_parity:
            return False
    return True