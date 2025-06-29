'''
Utility functions for the ID Card Gate application.
'''
def validate_input(value):
    '''
    Validates the input to ensure it is a positive integer.
    '''
    try:
        val = int(value)
        return val > 0
    except ValueError:
        return False
def validate_gate_range(value):
    '''
    Validates the gate range input to ensure it is in the correct format.
    '''
    try:
        l, r = map(int, value.split(','))
        return l <= r  # Ensure L is less than or equal to R
    except (ValueError, IndexError):
        return False