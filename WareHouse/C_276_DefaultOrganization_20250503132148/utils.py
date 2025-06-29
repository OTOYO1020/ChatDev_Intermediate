'''
Utility functions for generating and sorting permutations.
'''
from itertools import permutations
def generate_permutations(n):
    '''
    Generate all permutations of the sequence (1, 2, ..., N).
    '''
    if n < 1:
        return []  # Return an empty list for invalid n
    return list(permutations(range(1, n + 1)))
def sort_permutations(permutations):
    '''
    Sort the list of permutations in lexicographical order.
    '''
    return sorted(permutations)