'''
Module for ant simulation logic including position calculation and pass counting.
'''
def calculate_final_positions(N, T, S, X):
    '''
    Calculates the final positions of the ants based on their initial positions and directions.
    Parameters:
    N (int): The number of ants.
    T (float): The time duration.
    S (str): The binary string representing the direction of each ant.
    X (list): The list of initial coordinates for each ant.
    Returns:
    list: A sorted list of final positions of the ants.
    '''
    if len(S) != N:
        raise ValueError(f"Binary string S must be of length {N}.")
    if len(X) != N:
        raise ValueError(f"List X must contain {N} coordinates.")
    final_positions = []
    for i in range(N):  # Looping from 0 to N-1 as per Python's zero-based indexing
        if S[i] == '0':
            final_position = X[i] - (T + 0.1)
        else:
            final_position = X[i] + (T + 0.1)
        final_positions.append(final_position)
    final_positions.sort()
    return final_positions
def count_passes(final_positions):
    '''
    Counts the number of pairs of ants that pass each other.
    Parameters:
    final_positions (list): A sorted list of final positions of the ants.
    Returns:
    int: The count of pairs of ants that pass each other.
    '''
    pass_count = 0
    N = len(final_positions)
    for i in range(N):
        for j in range(i + 1, N):
            if final_positions[i] > final_positions[j]:
                pass_count += 1
    return pass_count