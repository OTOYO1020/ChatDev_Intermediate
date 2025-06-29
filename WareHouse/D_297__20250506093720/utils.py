'''
Utility functions for the application.
'''
def validate_input(a, b):
    '''
    Validates that both inputs are positive integers.
    '''
    return isinstance(a, int) and isinstance(b, int) and a > 0 and b > 0