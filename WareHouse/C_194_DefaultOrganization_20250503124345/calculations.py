'''
Module for calculating the sum of squared differences.
'''
def calculate_sum_squared_differences(N, A):
    # Initialize the cumulative sum of squared differences
    sum_squared_differences = 0
    # Iterate through all pairs of indices (i, j) where 0 <= j < i < N
    for i in range(N):  # Iterate from 0 to N-1
        for j in range(i):  # Iterate from 0 to i-1
            # Calculate the squared difference
            squared_difference = (A[i] - A[j]) ** 2  # No need to adjust index
            # Update the cumulative sum
            sum_squared_differences += squared_difference
    return sum_squared_differences