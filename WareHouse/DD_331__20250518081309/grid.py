'''
Grid class for managing the color grid and counting black squares.
'''
from typing import List, Tuple
class Grid:
    def __init__(self, N: int, grid_colors: List[List[str]]):
        self.N = N
        self.grid = grid_colors
        self.prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]
        # Build the prefix sum array
        for i in range(N):
            for j in range(N):
                self.prefix_sum[i + 1][j + 1] = (
                    self.prefix_sum[i][j + 1] +
                    self.prefix_sum[i + 1][j] -
                    self.prefix_sum[i][j] +
                    (1 if grid_colors[i][j] == 'B' else 0)
                )
    def count_black_squares(self, A: int, B: int, C: int, D: int) -> int:
        # Calculate the number of black squares using the prefix sum array
        total = 0
        # Calculate the number of complete grids in the range
        total_rows = (C // self.N) - (A // self.N) + 1
        total_cols = (D // self.N) - (B // self.N) + 1
        # Count full grids
        total += total_rows * total_cols * self.prefix_sum[self.N][self.N]
        # Count remaining parts
        for i in range(A % self.N, (C % self.N) + 1):
            for j in range(B % self.N, (D % self.N) + 1):
                if self.grid[i][j] == 'B':
                    total += 1
        return total
    def handle_query(self, queries: List[Tuple[int, int, int, int]]) -> List[int]:
        results = []
        for A, B, C, D in queries:
            # Input validation
            if A < 0 or B < 0 or C < 0 or D < 0 or A > C or B > D or C >= self.N * 200000 or D >= self.N * 200000:
                results.append(0)  # Return 0 for invalid queries
            else:
                results.append(self.count_black_squares(A, B, C, D))
        return results