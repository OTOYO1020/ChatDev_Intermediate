'''
Module containing the function to calculate sums of greater elements.
'''
from typing import List
def sum_greater_elements(A: List[int]) -> List[int]:
    '''
    Calculates the sum of all elements in A that are greater than each element A[i].
    Parameters:
    A (list of int): The list of integers.
    Returns:
    list of int: A list containing the sums for each element.
    '''
    max_value = 1000000  # Given constraint for A[i]
    frequency = [0] * (max_value + 1)
    total_sum = 0
    # Count frequency of each number and calculate total sum
    for number in A:
        frequency[number] += 1
        total_sum += number
    results = [0] * len(A)
    cumulative_sum = 0
    # Calculate the sum of elements greater than each unique number
    for i in range(max_value + 1):
        if frequency[i] > 0:
            # For each number, update the cumulative sum
            cumulative_sum += i * frequency[i]
            # Calculate the sum of elements greater than i
            greater_sum = total_sum - cumulative_sum
            # Assign this sum to all occurrences of this number in results
            for j in range(len(A)):
                if A[j] == i:
                    results[j] = greater_sum
    return results