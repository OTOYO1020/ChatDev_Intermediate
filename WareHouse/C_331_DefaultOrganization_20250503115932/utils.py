'''
Utility functions for the SumGreaterApp.
'''
def calculate_sums(A):
    '''
    Calculates the sum of elements greater than each element in the array A.
    Parameters:
    A (list): A list of integers.
    Returns:
    list: A list containing the sums of elements greater than each A[i].
    '''
    result = []
    for i in range(len(A)):
        sum_greater = 0  # Initialize sum_greater for each A[i]
        for j in range(len(A)):
            if A[j] > A[i]:  # Only add elements that are greater than A[i]
                sum_greater += A[j]
        result.append(sum_greater)  # Append the result for A[i]
    return result