'''
Module for generating non-decreasing sequences.
'''
from itertools import combinations_with_replacement
class SequenceGenerator:
    def __init__(self, N, M):
        self.N = N
        self.M = M
    def generate_sequences(self):
        # Generate all non-decreasing sequences of length N with values between 1 and M
        return list(combinations_with_replacement(range(1, self.M + 1), self.N))