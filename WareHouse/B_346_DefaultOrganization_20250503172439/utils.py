'''
Utility functions for validating input and checking substring formation.
'''
def validate_input(W, B):
    """
    Validate the input constraints for W and B.
    Ensure that 0 ≤ W, B ≤ 100 and W + B ≥ 1.
    """
    return 0 <= W <= 100 and 0 <= B <= 100 and (W + B) >= 1
def can_form_substring(W, B):
    """
    Determine if a substring with W occurrences of 'w' and B occurrences of 'b' can be formed.
    """
    S = 'wbwbwwbwbwbw'
    count_w = S.count('w')  # Count of 'w' in one cycle
    count_b = S.count('b')  # Count of 'b' in one cycle
    # Calculate maximum complete cycles
    max_complete_cycles = min(W // count_w if count_w > 0 else float('inf'),
                               B // count_b if count_b > 0 else float('inf'))
    # Total occurrences of 'w' and 'b' after maximum complete cycles
    total_w = max_complete_cycles * count_w
    total_b = max_complete_cycles * count_b
    # Remaining W and B after complete cycles
    remaining_W = W - total_w
    remaining_B = B - total_b
    # Check if the remaining requirements can be satisfied with the available characters in one cycle
    if remaining_W <= count_w and remaining_B <= count_b and remaining_W >= 0 and remaining_B >= 0:
        return 'YES'
    # Additional check to ensure that we can form the substring with the remaining characters
    if remaining_W > count_w or remaining_B > count_b:
        return 'NO'
    return 'YES' if remaining_W <= count_w and remaining_B <= count_b else 'NO'