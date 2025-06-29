'''
Module to calculate the cumulative sum based on the input integer.
'''
def calculate_sum(X):
    '''
    Function to calculate the cumulative sum of floor(X / 10^k) for k from 0 to 100.
    If X is negative, return 0.
    '''
    if X < 0:
        return 0  # Handle negative integers
    total_sum = 0
    power_of_ten = 1  # Start with 10^0
    for k in range(101):
        if power_of_ten > X:  # Avoid unnecessary calculations
            break
        total_sum += X // power_of_ten
        power_of_ten *= 10  # Update to the next power of ten
    return total_sum