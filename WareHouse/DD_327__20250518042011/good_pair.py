'''
Module containing the function to check if sequences A and B form a good pair.
'''
from typing import List
def is_good_pair(N: int, M: int, A: List[int], B: List[int]) -> str:
    if N < 1:
        return 'No'  # Return 'No' if N is less than 1
    if M < 0 or M > N:
        return 'No'  # Return 'No' if M is negative or exceeds N
    if M == 0:
        return 'Yes'  # No pairs to evaluate
    # Validate that A and B contain valid indices
    if any(a < 1 or a > N for a in A) or any(b < 1 or b > N for b in B):
        return 'No'  # Return 'No' if any index is out of bounds
    X = [-1] * N  # Initialize list with -1
    for i in range(M):
        a_index = A[i] - 1
        b_index = B[i] - 1
        if X[a_index] == -1 and X[b_index] == -1:
            # Both are unassigned, assign them different values
            X[a_index] = 0
            X[b_index] = 1
        elif X[a_index] == -1:
            # A is unassigned, assign it the opposite of B
            X[a_index] = 1 - X[b_index]
        elif X[b_index] == -1:
            # B is unassigned, assign it the opposite of A
            X[b_index] = 1 - X[a_index]
        else:
            # Both are assigned, check if they are different
            if X[a_index] == X[b_index]:
                return 'No'  # Return 'No' if both are assigned the same value
    return 'Yes'