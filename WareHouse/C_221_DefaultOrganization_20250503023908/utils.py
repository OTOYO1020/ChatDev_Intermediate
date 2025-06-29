'''
Utility functions for generating permutations and calculating products.
'''
from itertools import permutations
def generate_permutations(digits):
    '''
    Generate all unique permutations of the given digits.
    '''
    return set(permutations(digits))  # No filtering for leading zeros here
def calculate_product(A, B):
    '''
    Calculate the product of two integers A and B.
    '''
    return A * B