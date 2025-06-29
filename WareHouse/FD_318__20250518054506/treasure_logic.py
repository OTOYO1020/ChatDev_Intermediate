'''
Contains the logic for counting grabbable treasures based on coordinates and leg lengths.
'''
from typing import List
def count_grabbable_treasures(N: int, X: List[int], L: List[int]) -> int:
    '''
    Counts the number of valid integer positions k where the robot can grab all treasures.
    '''
    # Check if all leg lengths are zero
    if all(l == 0 for l in L):
        return 0 if N > 0 else 0  # No treasures can be grabbed if all leg lengths are zero
    valid_k_count = 0
    min_k = min(X)
    max_k = max(X)
    for k in range(min_k, max_k + 1):
        grabbed_treasures = set()  # Use a set to track grabbed treasure indices
        for i in range(N):
            leg_range = L[i]
            # Determine the range of treasures this leg can grab
            left_bound = k - leg_range
            right_bound = k + leg_range
            # Check which treasures can be grabbed by this leg
            for j in range(N):
                if left_bound <= X[j] <= right_bound:
                    grabbed_treasures.add(j)  # Add this treasure index to the set
        # Check if all treasures have been grabbed
        if len(grabbed_treasures) == N:
            valid_k_count += 1
    return valid_k_count