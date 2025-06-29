'''
Contains the logic for managing ball positions and calculating expected positions.
'''
from math import gcd
import random
class BallSwapper:
    def __init__(self, N):
        self.N = N
        self.positions = [0] + [1] * (N - 1)  # Black ball at index 0, white balls at indices 1 to N-1
    def get_expected_position(self, K):
        if K == 0:
            return 0  # If no swaps, expected position is 0
        if self.N == 1:
            return 0  # Only one ball, black ball is always at position 0
        # Initialize probabilities
        probabilities = [0] * self.N
        probabilities[0] = 1  # Black ball starts at position 0
        for _ in range(K):
            new_probabilities = [0] * self.N
            for a in range(1, self.N + 1):
                for b in range(1, self.N + 1):
                    if a != b:
                        # Swap positions a-1 and b-1
                        new_probabilities[a - 1] += probabilities[b - 1] / (self.N * (self.N - 1))
                        new_probabilities[b - 1] += probabilities[a - 1] / (self.N * (self.N - 1))
            probabilities = new_probabilities
        # Calculate expected position
        expected_position = sum(i * probabilities[i] for i in range(self.N))
        # Convert expected position to irreducible fraction P/Q
        P = expected_position
        Q = 1  # Since we are calculating the position directly
        # Calculate R such that R * Q ≡ P mod 998244353
        MOD = 998244353
        R = (P * pow(Q, MOD - 2, MOD)) % MOD  # Using Fermat's Little Theorem for modular inverse
        return R