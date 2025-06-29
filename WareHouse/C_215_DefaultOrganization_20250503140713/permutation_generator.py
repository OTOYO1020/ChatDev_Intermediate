'''
Module for generating distinct permutations of a string.
'''
from itertools import permutations
def generate_permutations(S):
    '''
    Generates all distinct permutations of the string S and returns them as a sorted list.
    '''
    perm_set = set(''.join(p) for p in permutations(S))
    sorted_permutations = sorted(perm_set)
    return sorted_permutations