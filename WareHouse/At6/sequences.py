'''
This file contains the Sequences class implementation.
'''
class Sequences:
    def __init__(self, A, B):
        self.A = A
        self.B = B
    def update_sequences(self, C):
        for i in range(len(self.A)):
            if self.A[i] == 0:
                self.A[i] = 1.0
        for i in range(len(self.B)):
            if self.B[i] == 0:
                self.B[i] = 1.0
        for i in range(len(C)):
            if C[i] == 0:
                C[i] = 1.0
        return self.A, self.B, C
    def find_common_ratio(self):
        ratio = 1.0
        for i in range(len(self.A)):
            if self.B[i] != 0:
                ratio = self.A[i] / self.B[i]
                break
        return ratio
    def multiply_sequence(self, C, ratio):
        for i in range(len(C)):
            C[i] *= ratio
        return C
    def perform_task(self, M):
        count = 0
        for i in range(len(self.A) - M + 1):
            subsequence = self.A[i:i + M]
            if subsequence == self.B:
                count += 1
        A, B, C = self.update_sequences(self.B)
        ratio = self.find_common_ratio()
        C = self.multiply_sequence(C, ratio)
        return count, A, B, C