'''
Module for calculating the resulting permutation from the input permutation.
'''
def calculate_permutation(p):
    """
    Calculate the resulting permutation Q based on the input permutation P.
    Parameters:
    p (list): A list of integers representing the permutation.
    Returns:
    list: The resulting permutation Q.
    """
    if not p:  # Check if the input list is empty
        return []
    n = len(p)
    q = [0] * n
    for i in range(1, n + 1):
        q[p[i - 1] - 1] = i  # Adjusting for zero-based indexing
    return q