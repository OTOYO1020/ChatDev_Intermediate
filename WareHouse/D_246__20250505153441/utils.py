'''
Utility functions for the application.
'''
def validate_input(input_value):
    '''
    Validates if the input is a valid non-negative integer.
    '''
    try:
        value = int(input_value)
        return value >= 0
    except ValueError:
        return False