'''
Module containing functions for majority operation and change calculation.
'''
import random  # Importing random for non-deterministic tie-breaking
def majority_operation(B):
    '''
    Perform the majority operation on a binary string B.
    Parameters:
    B (str): The binary string to process.
    Returns:
    str: A new binary string after applying the majority operation.
    '''
    if len(B) % 3 != 0:
        raise ValueError("Length of B must be a multiple of 3.")
    n = len(B) // 3
    C = ''
    for i in range(n):
        group = B[i*3:(i+1)*3]
        count_1 = group.count('1')
        count_0 = group.count('0')
        if count_1 > count_0:
            majority_value = '1'
        elif count_0 > count_1:
            majority_value = '0'
        else:
            # Non-deterministic tie-breaking strategy: randomly choose '0' or '1'
            majority_value = random.choice(['0', '1'])  
        C += majority_value
    return C
def calculate_min_changes(A, target):
    '''
    Calculate the minimum number of changes needed in A to achieve the desired target value.
    Parameters:
    A (str): The original binary string.
    target (str): The desired target value ('0' or '1').
    Returns:
    int: Minimum number of changes required.
    '''
    if target == '0':
        return A.count('1')  # Change all '1's to '0's
    else:
        return A.count('0')  # Change all '0's to '1's