'''
Utility functions for combinatorial calculations and input validation.
'''
def nCr(n, r):
    '''
    Calculate the number of combinations (n choose r).
    '''
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1
    r = min(r, n - r)  # Take advantage of symmetry
    numerator = 1
    denominator = 1
    for i in range(r):
        numerator *= (n - i)
        denominator *= (i + 1)
    return numerator // denominator
def validate_input(N, M, K, edges):
    '''
    Validate the input parameters for the graph.
    '''
    if not (2 <= N <= 200000):
        return False
    if not (1 <= M <= 200000):
        return False
    if not (0 <= K <= N):
        return False
    edge_set = set()
    for u, v in edges:
        if u < 1 or u > N or v < 1 or v > N or u == v:
            return False
        edge_set.add((min(u, v), max(u, v)))
    return len(edge_set) == len(edges)  # Ensure edges are unique