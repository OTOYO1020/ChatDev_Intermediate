'''
Matrix class to handle operations on a 2D matrix.
'''
class Matrix:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.matrix = [[0] * m for _ in range(n)]
    def update_columns(self, l: int, r: int, x: int):
        # Ensure l and r are within the bounds of the matrix
        l = max(0, min(l, self.m - 1))  # Adjust l to be within bounds
        r = max(0, min(r, self.m - 1))  # Adjust r to be within bounds
        # Check if l is greater than r after adjustment
        if l > r:
            return  # No columns to update
        for i in range(self.n):
            for j in range(l, r + 1):
                self.matrix[i][j] += x
    def replace_row(self, i: int, x: int):
        if 0 <= i < self.n:
            self.matrix[i] = [x] * self.m
    def get_value(self, i: int, j: int):
        if 0 <= i < self.n and 0 <= j < self.m:
            return self.matrix[i][j]
        return None  # Return None for out of bounds access