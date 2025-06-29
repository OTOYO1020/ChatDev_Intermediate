'''
Utility functions for string processing.
'''
def max_11_22_length(S: str) -> int:
    '''
    Finds the maximum length of a contiguous substring of S that is an 11/22 string.
    An 11/22 string has the following properties:
    - The first half consists of '1's.
    - The middle character is '/'.
    - The second half consists of '2's.
    Args:
    S (str): The input string to be analyzed.
    Returns:
    int: The maximum length of valid 11/22 substrings found.
    '''
    n = len(S)
    if n < 3 or n % 2 == 0:
        return 0  # Ensure valid length for 11/22 string
    if '/' not in S:
        return 0  # Ensure presence of '/'
    max_length = 0
    left_count = 0
    right_count = 0
    # Precompute the number of '1's to the left and '2's to the right
    left_counts = [0] * n
    right_counts = [0] * n
    # Count contiguous '1's from the left
    for i in range(n):
        if S[i] == '1':
            left_count += 1
        else:
            left_count = 0
        left_counts[i] = left_count
    # Count contiguous '2's from the right
    for i in range(n - 1, -1, -1):
        if S[i] == '2':
            right_count += 1
        else:
            right_count = 0
        right_counts[i] = right_count
    # Now check for '/' and calculate the maximum length
    for i in range(1, n - 1):
        if S[i] == '/':
            # Ensure that we have valid counts of '1's and '2's
            if left_counts[i - 1] > 0 and right_counts[i + 1] > 0:
                current_length = 2 * min(left_counts[i - 1], right_counts[i + 1]) + 1
                max_length = max(max_length, current_length)
    return max_length