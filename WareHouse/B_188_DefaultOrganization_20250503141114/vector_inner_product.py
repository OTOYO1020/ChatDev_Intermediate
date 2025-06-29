'''
This module contains the function to calculate the inner product of two vectors.
'''
def calculate_inner_product(a, b, n):
    '''
    Calculate the inner product of two vectors.
    Parameters:
    a (list of int): First vector.
    b (list of int): Second vector.
    n (int): The dimension of the vectors.
    Returns:
    str: "YES" if the inner product is zero, "NO" otherwise.
    '''
    inner_product = sum(a[i] * b[i] for i in range(n))
    return "YES" if inner_product == 0 else "NO"