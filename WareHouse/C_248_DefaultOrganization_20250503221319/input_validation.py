'''
Module for validating user input.
'''
def validate_input(N, M, K):
    '''
    Validates the user input for N, M, and K.
    Parameters:
    N (str): Input for the length of sequences.
    M (str): Input for the maximum value in sequences.
    K (str): Input for the maximum sum of sequences.
    Returns:
    bool: True if inputs are valid, False otherwise.
    '''
    try:
        N = int(N)
        M = int(M)
        K = int(K)
        return N > 0 and M > 0 and K >= N
    except ValueError:
        return False