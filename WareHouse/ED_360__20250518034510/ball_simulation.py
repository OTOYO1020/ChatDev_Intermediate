'''
Module for simulating the expected position of the black ball.
'''
import random
from fractions import Fraction
def expected_position(N: int, K: int) -> int:
    # Initialize probabilities
    probabilities = [0] * (N + 1)
    probabilities[1] = 1.0  # Starting at position 1
    for _ in range(K):
        new_probabilities = [0] * (N + 1)
        for i in range(1, N + 1):
            if probabilities[i] > 0:
                # Stay in the same position
                new_probabilities[i] += probabilities[i] * (N - 1) / N
                # Swap with every other position
                for j in range(1, N + 1):
                    if i != j:
                        new_probabilities[j] += probabilities[i] / (N - 1)  # Equal probability to each swap
        probabilities = new_probabilities
    # Calculate P and Q for the expected position
    P = sum(i * probabilities[i] for i in range(1, N + 1))
    Q = K  # Set Q to K, the number of operations
    # Handle case where Q might be zero
    if Q == 0:
        return 0  # If no operations, return 0
    return compute_modular_result(int(P), Q)
def compute_modular_result(P: int, Q: int) -> int:
    MOD = 998244353
    Q_inv = pow(Q, MOD - 2, MOD)  # Fermat's Little Theorem for modular inverse
    R = (P * Q_inv) % MOD
    return R