'''
Utility functions for input validation.
'''
def validate_input(value):
    '''
    Validates if the input value is a positive integer (greater than zero).
    '''
    try:
        int_value = int(value)
        return int_value > 0  # Ensure input is strictly greater than zero
    except ValueError:
        return False