'''
This file contains functions for data processing.
'''
from utils import find_matching_subsequences
def process_data(data):
    '''
    Process the given data and return the result.
    '''
    A = data['A']
    B = data['B']
    count = find_matching_subsequences(A, B)
    return count