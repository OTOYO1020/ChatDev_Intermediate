'''
Module to manage a sequence of integers, including updating and retrieving values.
'''
class SequenceManager:
    def __init__(self):
        self.sequence = []
    def set_sequence(self, sequence, N):
        if N <= 0:
            raise ValueError("N must be greater than 0.")
        if len(sequence) != N:  # Check if the length matches N
            raise ValueError(f"Expected sequence length of {N}, but got {len(sequence)}.")
        self.sequence = sequence
    def update_value(self, k, x):
        if 1 <= k <= len(self.sequence):
            self.sequence[k - 1] = x
        else:
            raise IndexError("Index out of bounds.")
    def print_value(self, k):
        if 1 <= k <= len(self.sequence):
            return self.sequence[k - 1]
        else:
            raise IndexError("Index out of bounds.")