'''
Contains the logic for counting valid card flips.
'''
from typing import List
def count_valid_flips(N: int, A: List[int], B: List[int]) -> int:
    mod = 998244353
    valid_count = 0
    # Handle the edge case when N is 1
    if N == 1:
        return 0 if A[0] == B[0] else 1
    # Iterate through all possible subsets of cards using bitmask
    for mask in range(1 << N):
        valid = True
        for i in range(N):
            current_flipped = (mask & (1 << i)) != 0
            if i < N - 1:  # Check adjacent cards only if not the last card
                next_flipped = (mask & (1 << (i + 1))) != 0
                # Check conditions for valid configurations
                if current_flipped and next_flipped:
                    if B[i] == B[i + 1]:
                        valid = False
                        break
                elif not current_flipped and not next_flipped:
                    if A[i] == A[i + 1]:
                        valid = False
                        break
                elif current_flipped and not next_flipped:
                    if B[i] == A[i + 1]:
                        valid = False
                        break
                elif not current_flipped and next_flipped:
                    if A[i] == B[i + 1]:
                        valid = False
                        break
        # Check the last card with the previous card
        if valid and N > 1:
            last_flipped = (mask & (1 << (N - 1))) != 0
            second_last_flipped = (mask & (1 << (N - 2))) != 0
            if last_flipped and not second_last_flipped:  # Last card flipped, previous not
                if B[N - 1] == A[N - 2]:
                    valid = False
            elif not last_flipped and second_last_flipped:  # Last card not flipped, previous flipped
                if A[N - 1] == B[N - 2]:
                    valid = False
        if valid:
            valid_count = (valid_count + 1) % mod
    return valid_count