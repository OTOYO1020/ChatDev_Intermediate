'''
Module for counting valid sequences based on given parameters N, M, and K.
'''
from itertools import product
def count_sequences(N: int, M: int, K: int) -> int:
    '''
    Count the number of valid sequences of length N with values between 1 and M
    such that the sum of the sequence is less than or equal to K.
    Parameters:
    N (int): Length of the sequence
    M (int): Maximum value in the sequence
    K (int): Maximum allowed sum of the sequence
    Returns:
    int: Count of valid sequences modulo 998244353
    '''
    count = 0
    # Generate all possible sequences of length N with values between 1 and M
    for sequence in product(range(1, M + 1), repeat=N):
        if sum(sequence) <= K:
            count += 1
            count %= 998244353  # To handle large numbers
    return count