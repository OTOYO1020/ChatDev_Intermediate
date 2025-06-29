'''
Module for bounce calculations including parsing input and calculating valid bounces.
'''
def parse_input(input_string):
    '''
    Parses the input string to extract N, L, and X.
    Expected format: "N, L1, L2, ..., LN, X"
    '''
    parts = input_string.split(',')
    N = int(parts[0].strip())
    if N < 0:
        raise ValueError("N must be a non-negative integer.")
    if len(parts) < N + 2:  # Ensure there are enough parts for L and X
        raise ValueError(f"Expected {N} elements in L and 1 element for X, but got {len(parts) - 1}.")
    if N == 0:
        L = []  # If N is 0, L should be an empty list
        X = int(parts[1].strip())  # X is the only element after N
    else:
        L = list(map(int, parts[1:N+1]))  # Adjusted to take the first N elements after N
        X = int(parts[N+1].strip())  # X is the element after the list L
    return N, L, X
def initialize_variables():
    '''
    Initializes the bounce coordinates list D with the first element as 0.
    '''
    D = [0]  # Initialize D with only the first element
    return D
def calculate_bounce_coordinates(N, L, D):
    '''
    Calculates the bounce coordinates based on the list L.
    '''
    if N > 0:  # Only calculate if there are bounce lengths
        for i in range(1, N + 1):
            D.append(D[i - 1] + L[i - 1])  # Append new bounce coordinates to D
def count_valid_bounces(D, X):
    '''
    Counts how many bounce coordinates are less than or equal to X.
    '''
    count = sum(1 for d in D if d <= X)
    return count
def get_result(D, X):
    '''
    Returns the count of valid bounces.
    '''
    return count_valid_bounces(D, X)