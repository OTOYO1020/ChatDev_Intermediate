'''
This module contains utility functions for the program.
'''
def find_subsequences(A, B):
    '''
    Find the number of subsequences in A that satisfy the given condition.
    Args:
        A (List[int]): The first sequence.
        B (List[int]): The second sequence.
    Returns:
        int: The number of subsequences that satisfy the condition.
    '''
    if len(B) > len(A):
        return 0
    count = 0
    # Initialize the window with the first M elements of A
    window = A[:len(B)]
    updated_B = [max(b, 1) for b in B]
    updated_window = [max(c, 1) for c in window]
    t = max(updated_B) / max(updated_window)
    scaled_window = [c * t for c in updated_window]
    # Check if the initial window satisfies the condition
    if all(abs(a - b) < 1e-9 for a, b in zip(scaled_window, updated_B)):
        count += 1
    # Slide the window through A and check each subsequence
    for i in range(len(B), len(A)):
        window.pop(0)
        window.append(A[i])
        updated_window = [max(c, 1) for c in window]
        t = max(updated_B) / max(updated_window)
        scaled_window = [c * t for c in updated_window]
        if all(abs(a - b) < 1e-9 for a, b in zip(scaled_window, updated_B)):
            count += 1
    return count