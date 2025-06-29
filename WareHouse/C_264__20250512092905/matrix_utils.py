'''
Utility functions for matrix transformation logic.
'''
from typing import List
from itertools import combinations
def canTransformMatrix(A: List[List[int]], B: List[List[int]]) -> bool:
    h1, w1 = len(A), len(A[0]) if A else 0
    h2, w2 = len(B), len(B[0]) if B else 0
    # Check if dimensions of B are less than or equal to those of A
    if h2 > h1 or w2 > w1:
        return False
    # Generate all possible submatrices of A
    row_indices = range(h1)
    col_indices = range(w1)
    for rows in combinations(row_indices, h2):
        for cols in combinations(col_indices, w2):
            submatrix = [[A[i][j] for j in cols] for i in rows]
            if submatrix == B:
                return True
    return False