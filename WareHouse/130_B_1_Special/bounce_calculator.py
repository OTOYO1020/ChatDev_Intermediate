'''
Module for calculating the number of bounces based on input parameters.
'''
def calculate_bounces(N, X, L):
    D = 0
    bounce_count = 0
    # Check the first bounce condition separately
    if 0 <= X:  # Check if the initial position is within the limit
        bounce_count += 1
    # Iterate over bounces starting from the first bounce (index 1)
    for i in range(1, N + 1):  # Iterate from 1 to N
        D += L[i - 1]  # Update D with the current bounce length
        if D <= X:  # Check the bounce condition after updating D
            bounce_count += 1
    return bounce_count