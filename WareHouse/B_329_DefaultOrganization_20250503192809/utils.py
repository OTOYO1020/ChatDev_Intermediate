'''
Utility functions for the Second Largest Finder application.
'''
def find_second_largest_value(numbers):
    '''
    Returns the second largest integer from a list of integers.
    '''
    if len(numbers) < 2:
        return None  # Not enough elements to find the second largest
    max_value = float('-inf')
    second_max = float('-inf')
    for number in numbers:
        if number > max_value:
            second_max = max_value  # Update second max before updating max
            max_value = number
        elif number > second_max and number < max_value:
            second_max = number
    return second_max if second_max != float('-inf') else None