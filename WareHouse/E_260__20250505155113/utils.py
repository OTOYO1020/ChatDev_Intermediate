'''
Utility functions for calculating good sequences.
'''
def calculate_good_sequences(M, pairs):
    '''
    Calculate the number of good sequences of lengths 1 to M based on the given pairs.
    Parameters:
    M (int): The maximum length of sequences.
    pairs (list of tuples): List of pairs (A_i, B_i) indicating valid positions.
    Returns:
    list: A list containing the count of good sequences for each length from 1 to M.
    '''
    good_count = [0] * M  # Initialize the good count array
    for A, B in pairs:
        good_count[A - 1] += 1  # Increment count for position A
        good_count[B - 1] += 1  # Increment count for position B
    f = [0] * M  # Initialize the result list for good sequences
    for k in range(1, M + 1):
        count = 0
        valid_length = 0
        for i in range(M):
            if good_count[i] > 0:
                valid_length += 1
            else:
                valid_length = 0
            # Count valid segments of exactly length k
            if valid_length == k:
                count += 1  # Count this segment as valid for length k
            elif valid_length > k:
                count += 1  # Count the segment of length k ending at i
        f[k - 1] = count  # Store the count for length k
    return f