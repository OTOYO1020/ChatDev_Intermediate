'''
Utility functions for sequence combination checking.
'''
def can_select_elements(A, B, C, X):
    """
    Check if any combination of elements from A, B, and C can sum to any element in X.
    Args:
    A (list): First sequence of integers.
    B (list): Second sequence of integers.
    C (list): Third sequence of integers.
    X (list): Sequence of target sums.
    Returns:
    list: A list of boolean values indicating if each element in X can be formed.
    """
    # Handle edge cases for empty lists
    if not A or not B or not C:
        return [False] * len(X)
    # Create a set of all possible sums from elements in A and B
    possible_sums = {a + b for a in A for b in B}  # Efficiently store sums in a set for O(1) lookup
    results = []
    # For each target sum in X, check if it can be formed by any combination of sums from A and B with elements from C
    for x in X:
        # Check if there exists a sum in possible_sums such that (x - c) is in possible_sums
        results.append(any((x - c) in possible_sums for c in C))  # Using any() for early exit
    return results