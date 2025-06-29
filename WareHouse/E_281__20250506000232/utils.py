'''
Utility functions for the sum calculation application.
'''
def sum_of_first_k(sorted_subarray, K):
    '''
    Calculate the sum of the first K elements in a sorted subarray.
    If K exceeds the length of the subarray, sum only the available elements.
    '''
    return sum(sorted_subarray[:min(K, len(sorted_subarray))])