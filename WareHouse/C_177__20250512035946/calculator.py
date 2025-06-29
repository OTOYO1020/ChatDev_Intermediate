'''
Module for calculating the sum of products of pairs.
'''
def calculate_sum_pairs(N: int, A: list) -> int:
    total_sum = 0
    MOD = 10**9 + 7
    # Iterate over all pairs (i, j) with i < j
    for i in range(N):
        for j in range(i + 1, N):
            total_sum += A[i] * A[j]
            total_sum %= MOD  # Update total_sum modulo MOD
    return total_sum