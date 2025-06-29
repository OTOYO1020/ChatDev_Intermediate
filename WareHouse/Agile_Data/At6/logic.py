'''
This file contains the logic implementation.
'''
from sequences import Sequences
class Logic:
    def __init__(self):
        pass
    def perform_task(self, A, B, M):
        sequences = Sequences(A, B)
        count, A, B, C = sequences.perform_task(M)
        return count, A, B, C