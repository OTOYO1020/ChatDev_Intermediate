'''
Utility functions for input validation.
'''
def validate_input(value: str) -> bool:
    """
    Validate if the input value is a positive integer within the specified range.
    Parameters:
    value (str): The input value as a string.
    Returns:
    bool: True if the value is a valid integer within the range 1 to 10^18, False otherwise.
    """
    try:
        num = int(value)
        return 1 <= num <= 10**18
    except ValueError:
        return False