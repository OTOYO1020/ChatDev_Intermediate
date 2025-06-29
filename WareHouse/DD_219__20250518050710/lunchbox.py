'''
Module containing the function to determine if lunchboxes can be purchased to meet requirements.
'''
from typing import List, Tuple
def can_buy_lunchboxes(N: int, X: int, Y: int, A: List[int], B: List[int]) -> Tuple[bool, int]:
    min_lunchboxes = float('inf')
    found_solution = False
    # Iterate through all combinations of lunchboxes using bit masking
    for i in range(1 << N):
        total_takoyaki = 0
        total_taiyaki = 0
        lunchbox_count = 0
        for j in range(N):
            if i & (1 << j):  # If the j-th lunchbox is included in the current combination
                total_takoyaki += A[j]
                total_taiyaki += B[j]
                lunchbox_count += 1
        # Check if the current combination meets the requirements
        if total_takoyaki >= X and total_taiyaki >= Y:
            found_solution = True
            min_lunchboxes = min(min_lunchboxes, lunchbox_count)
    if found_solution:
        return True, min_lunchboxes
    else:
        return False, -1  # Indicate no solution found by returning -1