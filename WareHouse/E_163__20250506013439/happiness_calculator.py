'''
Module for calculating maximum happiness points based on children's activeness values.
'''
import itertools
def calculate_max_happiness(activeness_values):
    max_happiness = 0
    # Create a list of tuples (original_index, value)
    indexed_values = list(enumerate(activeness_values))
    # Generate all permutations of the indexed values
    for permutation in itertools.permutations(indexed_values):
        current_happiness = 0
        # Calculate happiness points for the current permutation
        for new_index, (original_index, value) in enumerate(permutation):
            current_happiness += value * abs(original_index - new_index)  # Correctly using original_index
        # Update max_happiness if current_happiness is greater
        max_happiness = max(max_happiness, current_happiness)
    return max_happiness