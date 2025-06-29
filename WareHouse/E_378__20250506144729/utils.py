'''
Utility functions for input validation and sum calculation.
'''
def validate_input(n, m, a):
    '''
    Validate the input values.
    Parameters:
    n (int): The number of elements.
    m (int): The modulo value.
    a (list): The list of non-negative integers.
    Returns:
    bool: True if inputs are valid, False otherwise.
    '''
    if n <= 0 or m <= 0 or len(a) != n:
        return False
    if any(x < 0 for x in a):
        return False
    return True
def calculate_total_sum(a, m):
    '''
    Calculate the total sum of all subarray sums modulo m.
    Parameters:
    a (list): The list of non-negative integers.
    m (int): The modulo value.
    Returns:
    int: The total sum of all subarray sums modulo m.
    '''
    if not a:  # Check if the list is empty
        return 0
    total_sum = 0
    n = len(a)
    for l in range(1, n + 1):  # Start from 1 to n (1-based index)
        current_sum = 0
        for r in range(l, n + 1):  # Start from l to n (1-based index)
            current_sum += a[r - 1]  # Access the array with 0-based index
            mod_value = current_sum % m
            total_sum += mod_value
    return total_sum