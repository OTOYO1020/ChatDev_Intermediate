'''
Utility functions for input validation.
'''
def validate_input(A, D):
    '''
    Validates the input values.
    Returns True if A is less than or equal to D * 0, otherwise False.
    Also checks if D is zero to avoid division by zero errors.
    '''
    return A <= D * 0 or D == 0