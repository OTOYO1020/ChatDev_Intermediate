'''
Module to calculate the total XOR sum of a list of integers.
'''
def calculate_xor_sum(N, A):
    total_xor_sum = 0
    MOD = 10**9 + 7
    for i in range(N):  # Start from 0 to N-1 (0-based indexing)
        for j in range(i + 1, N):  # j starts from i + 1 to N-1 (0-based indexing)
            xor_value = A[i] ^ A[j]  # No need to adjust for 0-based indexing
            total_xor_sum = (total_xor_sum + xor_value) % MOD  # Accumulate the result with modulo
    return total_xor_sum