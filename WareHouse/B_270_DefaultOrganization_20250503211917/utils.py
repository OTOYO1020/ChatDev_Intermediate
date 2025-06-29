'''
Utility functions for input validation.
'''
def validate_input(value):
    '''
    Validates if the input value is an integer.
    '''
    try:
        int(value)
        return True
    except ValueError:
        return False