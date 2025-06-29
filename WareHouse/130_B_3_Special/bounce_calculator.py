'''
Contains functions for calculating bounces based on input parameters.
'''
def calculate_bounces(N, X, L):
    D = 0
    bounce_count = 0
    # Check the first bounce at coordinate 0
    if 0 <= X:
        bounce_count += 1
    # Iterate over bounces from index 1 to N
    for i in range(1, N + 1):  # Iterate from 1 to N (inclusive)
        D += L[i - 1]  # Update D using L[i-1]
        if D <= X:
            bounce_count += 1
    return bounce_count