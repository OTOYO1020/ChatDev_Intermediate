'''
Utility functions for the Square Pair Counter application.
'''
def validate_input(user_input: str) -> bool:
    '''
    Validates the user input to ensure it is a positive integer.
    '''
    try:
        value = int(user_input)
        return value > 0
    except ValueError:
        return False