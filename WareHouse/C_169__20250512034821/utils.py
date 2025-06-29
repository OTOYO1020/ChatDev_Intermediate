'''
Utility functions for input validation.
'''
import re
def validate_A(A):
    '''
    Validates that A is within the range of 0 to 10^15 inclusive.
    '''
    return 0 <= A <= 10**15
def validate_B(B_str):
    '''
    Validates that B is a float between 0 (inclusive) and 10 (exclusive) with exactly two decimal places.
    '''
    B_str = B_str.strip()  # Trim whitespace
    # Updated regular expression to match a float with exactly two decimal places
    pattern = r'^(0(\.00)?|[1-9]\d*(\.\d{2})?|0\.\d{2})$'  # Ensure exactly two decimal places
    if not re.match(pattern, B_str):  # Check format
        return False
    B = float(B_str)  # Convert to float for range check
    return 0 <= B < 10  # Check if B is within the valid range