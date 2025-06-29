'''
Game logic for calculating maximum stones removed by Takahashi.
'''
from typing import List
import bisect
def max_stones_removed(N: int, K: int, A: List[int]) -> int:
    '''
    Calculate the maximum stones Takahashi can remove.
    '''
    takahashi_stones = 0
    current_stones = N
    turn = 0  # 0 for Takahashi, 1 for Aoki
    while current_stones > 0:
        if turn == 0:  # Takahashi's turn
            # Find the largest option Takahashi can take
            index = bisect.bisect_right(A, current_stones) - 1
            if index >= 0:  # Valid move for Takahashi
                max_remove = A[index]
                takahashi_stones += max_remove
                current_stones -= max_remove  # Deduct stones after Takahashi's turn
            else:
                break  # No valid move for Takahashi, game ends
        else:  # Aoki's turn
            # Find the largest option Aoki can take
            index = bisect.bisect_right(A, current_stones) - 1
            if index >= 0:  # Valid move for Aoki
                max_remove = A[index]
                current_stones -= max_remove  # Deduct stones after Aoki's turn
            else:
                break  # No valid move for Aoki, game ends
        turn = 1 - turn  # Switch turns
    return takahashi_stones