'''
Utility functions for the bitwise AND and popcount calculator.
This module contains a function to calculate the number of 1s in the 
binary representation of a given integer.
'''
def popcount(x):
    '''
    Calculate the number of 1s in the binary representation of x.
    Parameters:
    x (int): The integer whose binary representation is to be analyzed.
    Returns:
    int: The count of 1s in the binary representation of x.
    '''
    return bin(x).count('1')