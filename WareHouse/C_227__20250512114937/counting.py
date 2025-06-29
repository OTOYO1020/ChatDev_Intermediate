'''
Module for counting valid triples (A, B, C) based on the given logic.
'''
def count_triples(N: int) -> int:
    """
    Count the number of valid triples (A, B, C) such that:
    1 <= A <= cube root of N
    A <= B <= square root of (N / A)
    B <= C <= N / (A * B)
    Parameters:
    N (int): The upper limit for calculating triples.
    Returns:
    int: The count of valid triples (A, B, C).
    """
    count = 0  # Initialize count of valid triples
    # Loop over possible values of A
    for A in range(1, int(N ** (1/3)) + 1):
        # Loop over possible values of B starting from A
        for B in range(A, int((N / A) ** 0.5) + 1):
            # Check if A * B exceeds N
            if A * B > N:  # Allow A * B to be equal to N
                break  # Exit the loop for B if A * B is too large
            # Calculate the maximum value of C
            C_max = N // (A * B)
            # Check if C_max is at least B
            if C_max >= B:
                # Count valid C values from B to C_max
                count += C_max - B + 1  # Ensure we only add positive counts
    return count