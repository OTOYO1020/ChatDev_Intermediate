'''
Module that contains the logic for calculating the factorial of a number.
'''
def calculate_factorial(x):
    """
    Calculate the smallest integer N such that N! = X.
    If X is less than 2, return None since no such N exists.
    """
    if x < 2:
        return None  # No such N exists for x < 2
    N = 1
    factorial = 1
    while factorial < x:  # Continue until factorial is less than x
        N += 1
        factorial *= N
    if factorial == x:  # Check if factorial equals x after the loop
        return N  # Return N if N! equals x
    return None  # No such N exists if factorial exceeds x