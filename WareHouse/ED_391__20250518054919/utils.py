'''
Utility functions for majority value calculations.
'''
def majority_value(group):
    """
    Returns the majority value (0 or 1) from a group of three binary digits.
    """
    return 1 if group.count('1') > group.count('0') else 0
def apply_operation(B):
    """
    Applies the majority operation to produce a new binary string.
    """
    C = ''
    for i in range(0, len(B), 3):
        group = B[i:i+3]
        majority = majority_value(group)
        C += str(majority)
    return C
def reduce_string(A, N):
    """
    Applies the apply_operation function N times to the input binary string A.
    """
    for _ in range(N):
        A = apply_operation(A)
    return A
def count_changes(A, target):
    """
    Counts the minimum number of changes required to change the original string A to a specified target value (0 or 1).
    This function compares each character in A to the target.
    """
    if target not in ('0', '1'):
        raise ValueError("Target must be '0' or '1'")
    # Count the number of characters in A that do not match the target
    return sum(1 for char in A if char != target)