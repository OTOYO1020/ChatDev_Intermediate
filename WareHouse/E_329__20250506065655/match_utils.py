'''
Utility functions for string matching operations.
'''
def can_match(X, S, T, N, M):
    """
    Determine if a string X of length N filled with '#' can be transformed to match S
    by replacing M consecutive characters with T.
    """
    if M > N:
        return False  # Early exit if T is longer than X
    for start_index in range(N - M + 1):
        # Create a modified version of X by replacing M characters starting from start_index with T
        modified_X = list(X)  # Convert to list for mutability
        modified_X[start_index:start_index + M] = T  # Replace M characters with T
        modified_X = ''.join(modified_X)  # Convert back to string
        # Check if the modified X matches S
        if modified_X == S:
            return True
    return False