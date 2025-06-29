'''
Module for calculating maximum production capacity based on given parameters.
'''
from typing import List
def max_production_capacity(N: int, A: List[int], B: List[int], P: List[int], Q: List[int], X: int) -> int:
    '''
    Calculate the maximum achievable production capacity.
    '''
    # Validate input lengths
    if len(A) != N or len(B) != N or len(P) != N or len(Q) != N:
        raise ValueError("The length of A, B, P, and Q must match N.")
    # Validate non-negative values
    if any(a < 0 for a in A) or any(b < 0 for b in B) or any(p < 0 for p in P) or any(q < 0 for q in Q):
        raise ValueError("Processing rates and prices must be non-negative.")
    min_capacity = float('inf')  # Initialize to a very high value
    for i in range(N):  # Iterate over each process
        for machines_S in range(X // P[i] + 1):  # Iterate through all possible machines of type S
            remaining_budget = X - (machines_S * P[i])
            if remaining_budget >= 0:
                machines_T = remaining_budget // Q[i] if Q[i] > 0 else 0  # Calculate max machines of type T
                W_i = (machines_S * A[i]) + (machines_T * B[i])  # Calculate production capacity
                min_capacity = min(min_capacity, W_i)  # Update min_capacity
    return min_capacity if min_capacity != float('inf') else 0  # Return the minimum production capacity or 0 if no machines can be purchased