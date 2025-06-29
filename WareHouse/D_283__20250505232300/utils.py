'''
Utility functions for input validation.
'''
def validate_input(input_string):
    '''
    Validates the input string to ensure it consists only of lowercase letters and parentheses.
    '''
    return all(c.islower() or c in '()' for c in input_string)