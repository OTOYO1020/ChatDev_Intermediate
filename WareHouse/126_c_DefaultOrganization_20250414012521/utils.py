'''
Utility functions for calculating the probability based on doubling logic.
'''
def num_twice(A, K):
    # Validate K
    if K <= 0:
        raise ValueError("K must be a natural number greater than 0.")
    # Return 0 if A is already greater than or equal to K
    if A >= K:
        return 0
    count = 0
    while A < K:
        A *= 2
        count += 1
    return count
def calculate_probability(N, K):
    probability = 0
    for i in range(1, N + 1):
        num = num_twice(i, K)
        probability += (1 / N) * (1 / 2) ** num
    return probability