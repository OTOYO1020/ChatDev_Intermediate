'''
Utility functions for the main application.
'''
def find_min_non_negative(A_set):
    '''
    Finds the minimum non-negative integer not present in the given set.
    '''
    min_non_negative = 0
    while min_non_negative in A_set:
        min_non_negative += 1
    return min_non_negative