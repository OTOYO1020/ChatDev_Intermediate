'''
Utility functions for calculating the minimum operations needed
to make '1's contiguous in a given string.
'''
def count_min_operations(N, S):
    count_ones = S.count('1')
    positions = [i for i, char in enumerate(S) if char == '1']
    if count_ones == 0:
        return 0  # No '1's to move
    # Calculate the target positions for contiguous '1's
    target_positions = [positions[0] + j for j in range(count_ones)]
    min_operations = 0
    for j in range(count_ones):
        # Calculate the number of moves needed to shift '1's to target positions
        min_operations += abs(positions[j] - target_positions[j])  # Use abs() for correct calculation
    return min_operations