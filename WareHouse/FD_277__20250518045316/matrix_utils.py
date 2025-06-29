'''
Utility functions for matrix processing.
'''
from typing import List
def can_matrix_be_sorted(H: int, W: int, A: List[List[int]]) -> bool:
    unique_positive_integer = 1
    used_integers = set()  # To track used integers
    # Collect existing positive integers in the matrix
    for row in A:
        for value in row:
            if value > 0:
                used_integers.add(value)
    for i in range(H):
        for j in range(W):
            if A[i][j] == 0:
                # Find the next unique positive integer
                while unique_positive_integer in used_integers:
                    unique_positive_integer += 1
                A[i][j] = unique_positive_integer
                used_integers.add(unique_positive_integer)
                unique_positive_integer += 1
    return is_matrix_sorted(A)
def is_matrix_sorted(A: List[List[int]]) -> bool:
    H = len(A)
    W = len(A[0])
    # Check the sorting condition for all pairs of rows
    for i in range(H):
        for i_prime in range(i + 1, H):
            for j in range(W):
                if A[i][j] > A[i_prime][j]:
                    return False
    # Check the sorting condition for all pairs of columns in the same row
    for i in range(H):
        for j in range(W):
            for j_prime in range(j + 1, W):
                if A[i][j] > A[i][j_prime]:
                    return False
    return True