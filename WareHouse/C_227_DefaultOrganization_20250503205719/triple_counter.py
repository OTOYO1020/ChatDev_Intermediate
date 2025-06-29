'''
Module for calculating the count of valid triples (A, B, C).
'''
def calculate_triples(N):
    """
    Calculate the count of valid triples (A, B, C) such that:
    1 <= A <= N^(1/3)
    A <= B <= N^(1/2)
    B <= C <= floor(N / (A * B))
    Parameters:
    N (int): A positive integer input.
    Returns:
    int: The count of valid triples.
    """
    count = 0
    for A in range(1, int(N**(1/3)) + 1):
        for B in range(A, int(N**(1/2)) + 1):
            C_max = N // (A * B)
            if C_max >= B:
                count += C_max - B + 1
    return count