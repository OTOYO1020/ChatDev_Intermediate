'''
Utility functions for input validation.
'''
def validate_input(weights, threshold):
    if not weights or threshold <= 0:
        return False
    return True