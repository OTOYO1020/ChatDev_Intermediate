'''
Module for validating the input string based on specific criteria.
Ensures S contains only the allowed characters and checks the counts and positions.
'''
def validate_input(S: str) -> str:
    '''
    Validates the string S according to the specified rules.
    Ensures S contains only the allowed characters and checks the counts and positions.
    '''
    S = S.strip()  # Trim whitespace from the input string
    if len(S) != 8:  # Re-check the length after trimming
        return 'INVALID: Length must be exactly 8 characters. Please enter a string with exactly 8 characters.'
    # Check for invalid characters
    allowed_characters = set('KQRBN')
    if any(char not in allowed_characters for char in S):
        return 'INVALID: Contains invalid characters. Only K, Q, R, B, N are allowed. Please check your input.'
    # Count occurrences of each character
    counts = {char: S.count(char) for char in allowed_characters}
    # Validate counts
    if counts['K'] != 1 or counts['Q'] != 1 or counts['R'] != 2 or counts['B'] != 2 or counts['N'] != 2:
        return 'INVALID: The string must contain exactly one \'K\', one \'Q\', two \'R\'s, two \'B\'s, and two \'N\'s. Please check your input.'
    # Identify positions of 'B' characters
    positions_B = [i for i, char in enumerate(S) if char == 'B']
    if len(positions_B) != 2:
        return 'INVALID: Incorrect number of \'B\' characters. Expected 2.'
    # Check if both 'B' characters have the same parity
    if positions_B[0] % 2 == positions_B[1] % 2:
        return 'INVALID: Both \'B\' characters have the same parity.'
    # Identify positions of 'R' characters
    positions_R = [i for i, char in enumerate(S) if char == 'R']
    if len(positions_R) != 2:
        return 'INVALID: Incorrect number of \'R\' characters. Expected 2.'
    # Identify position of 'K' character
    positions_K = [i for i, char in enumerate(S) if char == 'K']
    if len(positions_K) != 1:  # Ensure only one 'K' exists
        return 'INVALID: Incorrect number of \'K\' characters. Expected 1.'
    position_K = positions_K[0]  # Get the index of 'K'
    # Ensure 'K' is positioned between the two 'R's
    if not (positions_R[0] < position_K < positions_R[1]):
        return 'INVALID: \'K\' is not positioned between the two \'R\' characters.'
    return 'VALID'