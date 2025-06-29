'''
Module for counting valid sequences based on input constraints.
'''
from typing import List
def count_sequences(N: int, C: List[int]) -> int:
    MOD = 10**9 + 7
    used = set()  # Track used integers
    total_sequences = 1
    for i in range(N):
        valid_choices = 0
        # Count valid choices for A[i]
        for j in range(1, C[i] + 1):
            if j not in used:
                valid_choices += 1
        if valid_choices == 0:
            return 0
        # Multiply the total sequences by the number of valid choices
        total_sequences = (total_sequences * valid_choices) % MOD
        # Add the first valid choice to used
        for j in range(1, C[i] + 1):
            if j not in used:
                used.add(j)  # Add valid choice to used
                break  # Stop after adding one valid choice
    return total_sequences