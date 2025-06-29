'''
Utility functions for number validation and rounding down.
'''
def is_valid_number(x):
    """
    Validates if the input x is a valid number (integer or decimal).
    It checks for leading zeros and ensures the decimal part is valid.
    """
    # Check if the input is empty
    if not x:
        return False
    # Check for negative numbers
    is_negative = x.startswith('-')
    if is_negative:
        if len(x) == 1:  # Only '-' is invalid
            return False
        x = x[1:]  # Remove the negative sign for validation
    # Ensure there are no leading zeros in the integer part
    if x.startswith('0') and len(x) > 1 and '.' not in x:
        return False
    # Validate the number without the negative sign
    if '.' in x:
        int_part, dec_part = x.split('.')
        # Adjusted check for leading zeros in negative decimals
        if int_part == '0' and len(dec_part) > 0:
            return False  # Invalid if it is like 0.x
        if int_part.startswith('0') and len(int_part) > 1:
            return False  # Invalid if it has leading zeros like 01.x
        return (int_part.isdigit() and
                dec_part.isdigit())  # Ensure decimal part is valid
    else:
        return x.isdigit() and (x == '0' or not x.startswith('0'))  # Check leading zero
def round_down_value(x):
    """
    Rounds down the input number x by converting the integer part to int.
    If x is a decimal, it discards the decimal part.
    """
    if '.' in x:
        int_part, _ = x.split('.')
        return int(int_part)  # Convert to int to round down
    else:
        return int(x)  # Already an integer