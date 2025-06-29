'''
Contains utility functions for common tasks.
'''
def validate_input(n, k):
    if not (1 <= k < n <= 1000) or k % 2 == 0:
        raise ValueError("K must be an odd number and 1 ≤ K < N ≤ 1000.")