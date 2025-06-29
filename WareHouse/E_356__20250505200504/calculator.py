'''
Module for calculating the nested summation based on the input sequence.
'''
import math
def calculate_sum(N, A):
    '''
    Calculate the total sum of the nested summation for the sequence A.
    Parameters:
    N (int): Length of the sequence.
    A (list): List of integers representing the sequence.
    Returns:
    int: Total sum of the nested summation.
    Note: The indices used in this function are zero-based, 
    while the task description uses one-based indexing.
    '''
    total_sum = 0
    for i in range(N - 1):  # Start from 0 to N-2
        for j in range(i + 1, N):  # Inner loop starts from i + 1 to N
            max_value = max(A[i], A[j])  # Accessing elements using zero-based index
            min_value = min(A[i], A[j])  # Accessing elements using zero-based index
            # Ensure min_value is not zero to avoid division by zero
            if min_value == 0:
                continue  # Skip this iteration if min_value is zero
            ratio = max_value / min_value
            floor_value = math.floor(ratio)
            total_sum += floor_value
    return total_sum