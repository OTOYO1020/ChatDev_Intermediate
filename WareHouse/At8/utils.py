'''
This file contains utility functions and classes.
'''
def find_matching_indices(A, B, M):
    count = 0
    for i in range(len(A) - M + 1):
        C = A[i:i + M]
        updated_B = [x if x != 0 else 1 for x in B]
        updated_C = [x * (updated_B[i] / C[i]) for i, x in enumerate(C) if C[i] != 0]
        if updated_B == updated_C:
            count += 1
    return count