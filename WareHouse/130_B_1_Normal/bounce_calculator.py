'''
Module for bounce calculation logic.
'''
def parse_input(n_str, l_str, x_str):
    N = int(n_str)
    if not l_str.strip():  # Check if the input for L is empty
        raise ValueError("The list of integers L cannot be empty.")
    try:
        L = list(map(int, l_str.split(',')))  # Attempt to convert to integers
    except ValueError:
        raise ValueError("All elements in the list L must be integers.")
    X = int(x_str)
    # Validate that the length of L matches N
    if len(L) != N:
        raise ValueError("The length of list L must be equal to N.")
    return N, L, X
def initialize_variables():
    """
    Initializes the bounce coordinates with the starting point.
    Returns:
        list: A list containing the initial bounce coordinate (0).
    """
    return [0]
def calculate_bounce_coordinates(N, L):
    """
    Calculates the bounce coordinates based on the number of bounces and the list of bounce distances.
    Parameters:
        N (int): The number of bounces.
        L (list): A list of integers representing the distances of each bounce.
    Returns:
        list: A list of bounce coordinates.
    """
    D = initialize_variables()
    if N < 0:
        raise ValueError("N must be greater than or equal to 0.")
    if N == 0:
        return []  # Return an empty list if there are no bounces
    if N > len(L):
        raise ValueError("N cannot be greater than the length of list L.")
    for i in range(N):
        D.append(D[i] + L[i])
    return D
def count_valid_bounces(D, X):
    """
    Counts how many bounce coordinates are less than or equal to X.
    Parameters:
        D (list): A list of bounce coordinates.
        X (int): The maximum coordinate to compare against.
    Returns:
        int: The count of valid bounces.
    """
    return sum(1 for d in D if d <= X)
def get_result(count):
    """
    Formats the result for output.
    Parameters:
        count (int): The count of valid bounces.
    Returns:
        str: A formatted string with the result.
    """
    return f"Number of valid bounces: {count}"