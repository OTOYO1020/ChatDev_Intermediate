'''
Grid class for calculating values and sums in the grid.
'''
from typing import List, Tuple
from utils import modulo
class Grid:
    def __init__(self, N: int, M: int):
        self.N = N
        self.M = M
    def get_value(self, i: int, j: int) -> int:
        return (i - 1) * self.M + j
    def sum_range(self, A: int, B: int, C: int, D: int) -> int:
        # Return 0 if the column range is invalid
        if C > D:
            return 0
        total_sum = 0
        for i in range(A, B + 1):
            for j in range(C, D + 1):
                if (i + j) % 2 == 0:  # Include the value only if (i+j) is even
                    total_sum += self.get_value(i, j)
        return modulo(total_sum)  # Use the modulo function from utils