'''
Module containing the can_match function to check if T can match within S.
'''
def can_match(S: str, T: str) -> bool:
    '''
    Checks if string T can be placed in string S at any position.
    Parameters:
    S (str): The main string where we check for matches.
    T (str): The string we want to match within S.
    Returns:
    bool: True if T can match within S, False otherwise.
    '''
    N = len(S)
    M = len(T)
    # Edge case: if T is longer than S, return False
    if M > N:
        return False
    # Initialize X with '#' characters
    X = '#' * N
    # Iterate over all possible starting positions
    for start in range(N - M + 1):
        # Create the modified string by replacing the relevant section
        modified_X = X[:start] + T + X[start + M:]
        # Check if modified_X matches S
        if modified_X == S:
            return True
    return False