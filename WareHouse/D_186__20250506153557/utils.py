'''
Utility functions for calculating the total sum of absolute differences.
'''
def calculate_total_sum(array):
    total_sum = 0
    n = len(array)
    array.sort()  # Sort the array to facilitate absolute difference calculation
    for i in range(n - 1):  # Loop from 0 to N-2
        for j in range(i + 1, n):  # Loop from i+1 to N-1
            diff = array[j] - array[i]  # Calculate the absolute difference
            total_sum += diff  # Update total_sum with the difference
    return total_sum