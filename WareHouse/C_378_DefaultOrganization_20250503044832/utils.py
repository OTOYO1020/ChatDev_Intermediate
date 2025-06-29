'''
Utility functions for processing the sequence of integers.
'''
def find_recent_positions(N, A):
    last_seen = {}
    B = [-1] * N
    for i in range(N):
        if A[i] in last_seen:
            B[i] = last_seen[A[i]]
        last_seen[A[i]] = i
    return B