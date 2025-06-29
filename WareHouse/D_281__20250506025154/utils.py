'''
Utility functions for generating sums and finding maximum multiples.
'''
from itertools import combinations
def generate_sums(A, K):
    '''
    Generate all possible sums of K distinct elements from the list A.
    '''
    return {sum(comb) for comb in combinations(A, K)}
def find_max_multiple(sums, D):
    '''
    Find the maximum multiple of D from the generated sums.
    '''
    max_multiple = -1
    for s in sums:
        if s % D == 0:
            max_multiple = max(max_multiple, s)
    return max_multiple