'''
Utility functions for input validation.
'''
def validate_input(A, X, M):
    '''
    Validates that A is a positive integer, X is a non-negative integer, and M is a positive integer.
    Returns True if all conditions are met, otherwise returns False.
    '''
    return (isinstance(A, int) and A > 0 and 
            isinstance(X, int) and X >= 0 and 
            isinstance(M, int) and M > 0)