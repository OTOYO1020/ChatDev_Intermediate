'''
Utility functions for the subsequence calculator.
This module contains helper functions used in the main application.
'''
def binary_search(sorted_list, value):
    """
    Perform binary search to find the count of elements less than or equal to 'value'.
    Parameters:
    sorted_list (list): The sorted list of integers.
    value (int): The value to search for in the sorted list.
    Returns:
    int: The count of elements in sorted_list that are less than or equal to value.
    """
    low, high = 0, len(sorted_list)
    while low < high:
        mid = (low + high) // 2
        if sorted_list[mid] <= value:
            low = mid + 1
        else:
            high = mid
    return low