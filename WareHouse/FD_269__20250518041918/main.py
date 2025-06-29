'''
Main entry point for the grid sum application.
'''
from typing import List, Tuple
from grid import Grid
class MainApp:
    def __init__(self):
        self.N = 0
        self.M = 0
        self.queries = []
    def setup_input(self, N: int, M: int, queries: List[Tuple[int, int, int, int]]):
        self.N = N
        self.M = M
        self.queries = queries
    def calculate_sum(self) -> List[int]:
        grid = Grid(self.N, self.M)
        results = []
        for A, B, C, D in self.queries:
            # Validate input ranges
            if A < 1 or B > self.N or C < 1 or D > self.M or A > B or C > D:
                results.append(0)  # Return 0 for invalid ranges
                continue
            total_sum = grid.sum_range(A, B, C, D)
            results.append(total_sum)
        return results
if __name__ == "__main__":
    app = MainApp()
    # Example usage
    app.setup_input(5, 5, [(1, 3, 1, 3), (2, 4, 2, 4)])  # Sample input
    results = app.calculate_sum()
    print(results)  # Output results