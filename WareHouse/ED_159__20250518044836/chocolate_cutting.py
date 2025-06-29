'''
Contains the logic for calculating the minimum cuts needed for the chocolate bar.
'''
from typing import List
from itertools import combinations
def min_cuts(H: int, W: int, K: int, S: List[List[int]]) -> int:
    '''
    Calculate the minimum number of cuts needed to ensure that each block of chocolate
    has K or fewer white squares.
    '''
    def count_white_squares(prefix_sum, x1, y1, x2, y2):
        return prefix_sum[x2][y2] - prefix_sum[x1][y2] - prefix_sum[x2][y1] + prefix_sum[x1][y1]
    # Create a prefix sum array
    prefix_sum = [[0] * (W + 1) for _ in range(H + 1)]
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            prefix_sum[i][j] = S[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]
    # Check if the entire chocolate bar is already valid
    if count_white_squares(prefix_sum, 0, 0, H, W) <= K:
        return 0
    # Edge case: If H or W is 1, we can only have one block
    if H == 1 or W == 1:
        return 0 if count_white_squares(prefix_sum, 0, 0, H, W) <= K else float('inf')
    min_cuts_needed = float('inf')
    # Generate all possible cut positions
    for h_cuts in range(H + 1):  # Number of horizontal cuts
        for v_cuts in range(W + 1):  # Number of vertical cuts
            for h_positions in combinations(range(1, H), h_cuts):
                for v_positions in combinations(range(1, W), v_cuts):
                    # Include the edges
                    h_positions_full = [0] + list(h_positions) + [H]
                    v_positions_full = [0] + list(v_positions) + [W]
                    valid = True
                    # Check each block defined by cut positions
                    for i in range(len(h_positions_full) - 1):
                        for j in range(len(v_positions_full) - 1):
                            if count_white_squares(prefix_sum, h_positions_full[i], v_positions_full[j], h_positions_full[i + 1], v_positions_full[j + 1]) > K:
                                valid = False
                                break
                        if not valid:
                            break
                    if valid:
                        cuts = len(h_positions_full) - 1 + len(v_positions_full) - 1  # Count the number of cuts made
                        min_cuts_needed = min(min_cuts_needed, cuts)
    return min_cuts_needed if min_cuts_needed != float('inf') else 0