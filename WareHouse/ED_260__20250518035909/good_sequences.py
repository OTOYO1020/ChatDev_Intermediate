'''
Module to count good sequences based on given pairs and maximum integer.
'''
from typing import List, Tuple
def count_good_sequences(M: int, pairs: List[Tuple[int, int]]) -> List[int]:
    '''
    Count good sequences of lengths from 1 to M based on the provided pairs.
    Parameters:
    M (int): The maximum integer defining the length of sequences.
    pairs (List[Tuple[int, int]]): A list of tuples containing pairs of integers.
    Returns:
    List[int]: A list containing the counts of good sequences for each length from 1 to M.
    '''
    f = [0] * M  # Initialize the list to store counts of good sequences
    valid_set = set()  # Set to store valid integers from pairs
    # Populate the valid_set with all integers from pairs
    for a, b in pairs:
        valid_set.add(a)
        valid_set.add(b)
    for k in range(1, M + 1):  # Iterate through lengths from 1 to M
        count = 0
        # Generate all contiguous subsequences of length k
        for start in range(1, M - k + 2):  # Start of the subsequence (1 to M-k+1)
            end = start + k - 1  # End of the subsequence
            # Create the actual subsequence using the range of integers
            subsequence = set(range(1, M + 1)[start - 1:end])  # Corrected line
            # Check if the subsequence contains at least one of the integers from each pair
            if all(any(x in subsequence for x in pair) for pair in pairs):
                count += 1
        f[k - 1] = count  # Store the count for length k
    return f