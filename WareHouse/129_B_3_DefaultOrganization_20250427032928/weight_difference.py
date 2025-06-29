'''
Module for calculating the minimum absolute difference between two partitions of weights.
'''
def calculate_min_difference(weights):
    n = len(weights)
    min_difference = float('inf')
    # Loop over each possible division point T from 1 to N-1 (0 to n-2 in 0-indexing)
    for T in range(1, n):
        # Calculate S_1 as the sum of weights from index 0 to T-1 (1 to T in 1-indexing)
        S_1 = sum(weights[:T])
        # Calculate S_2 as the sum of weights from index T to N-1 (T+1 to N in 1-indexing)
        S_2 = sum(weights[T:])
        # Compute the absolute difference between S_1 and S_2
        difference = abs(S_1 - S_2)
        # Update min_difference if the current difference is smaller
        if difference < min_difference:
            min_difference = difference
    return min_difference