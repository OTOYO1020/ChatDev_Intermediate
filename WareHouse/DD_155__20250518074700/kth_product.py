'''
Module to calculate the K-th product of pairs from a list.
'''
from typing import List
def find_kth_product(N: int, K: int, A: List[int]) -> int:
    '''
    Computes the K-th product of all unique pairs (i, j) where 1 <= i < j <= N.
    Parameters:
    N (int): The number of elements in the list A.
    K (int): The 1-based index of the product to retrieve.
    A (List[int]): The list of integers.
    Returns:
    int: The K-th product in sorted order of products.
    '''
    if N <= 0:
        raise ValueError("N must be a positive integer.")
    if K <= 0:
        raise ValueError("K must be a positive integer.")
    if N < 2:
        raise ValueError("N must be at least 2 to form pairs.")
    if K < 1 or K > (N * (N - 1)) // 2:
        raise ValueError("K must be within the valid range of products.")
    # Validate that A contains exactly N integers
    if len(A) != N:
        raise ValueError("Length of A must be equal to N.")
    # Validate that A contains unique integers
    if len(A) != len(set(A)):
        raise ValueError("All elements in A must be unique.")
    products = []  # Use a list to store all products
    for i in range(N):
        for j in range(i + 1, N):
            products.append(A[i] * A[j])  # Add products to the list
    products.sort()  # Sort the list of products
    # Check if K is valid after sorting
    if K > len(products):
        raise ValueError("K exceeds the number of products generated.")
    return products[K - 1]