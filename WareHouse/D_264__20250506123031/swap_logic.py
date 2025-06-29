'''
Module containing the logic to count the number of swaps needed to transform
a permutation of 'atcoder' into 'atcoder'.
'''
def count_swaps(S):
    '''
    Counts the number of adjacent swaps needed to transform the input string S
    into the target string 'atcoder'.
    Parameters:
    S (str): A permutation of the string 'atcoder'.
    Returns:
    int: The minimum number of swaps required.
    Raises:
    ValueError: If S is not a permutation of 'atcoder'.
    '''
    target = "atcoder"
    if sorted(S) != sorted(target):
        raise ValueError("Input string must be a permutation of 'atcoder'.")
    operations = 0
    S = list(S)
    for i in range(len(target)):
        while S[i] != target[i]:
            # Find the index of the target character in S
            index = S.index(target[i])  # Find the first occurrence of the target character
            # Swap with the adjacent character to the left until it reaches the correct position
            if index > i:  # Only swap if the index is greater than i
                for j in range(index, i, -1):  # Iterate backwards
                    S[j], S[j - 1] = S[j - 1], S[j]  # Swap with the adjacent character to the left
                    operations += 1
            else:
                break  # Exit if the character is already in the correct position
    return operations