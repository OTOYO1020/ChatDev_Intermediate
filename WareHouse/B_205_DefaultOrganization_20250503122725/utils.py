'''
Utility file containing the logic to check for permutations.
'''
def is_permutation(n, sequence):
    '''
    Checks if the given sequence is a permutation of numbers from 1 to n.
    Parameters:
    n (int): The number of elements expected in the permutation.
    sequence (list): The list of integers to check.
    Returns:
    bool: True if the sequence is a permutation, False otherwise.
    '''
    if n == 0:  # Handle the case where n is 0
        return len(sequence) == 0  # Ensure the sequence is also empty
    seen = [False] * (n + 1)  # Initialize a boolean array of size N+1
    for num in sequence:
        if 1 <= num <= n:
            if seen[num]:  # Check for duplicates
                return False
            seen[num] = True  # Mark the number as seen
        else:
            return False
    # Check if all numbers from 1 to n are present in the seen array
    return all(seen[1:n + 1])  # Check from index 1 to n