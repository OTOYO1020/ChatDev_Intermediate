'''
Utility class for validating the 3x3 grid.
'''
import itertools
class GridValidator:
    def __init__(self, grid):
        self.grid = grid
    def is_valid(self):
        # Check rows for duplicates and ensure no row contains the same number in all three cells
        for row in self.grid:
            if len(set(row)) == 1:  # Check if all three numbers are the same
                return False
        # Check columns for duplicates and ensure no column contains the same number in all three cells
        for col in range(3):
            column_values = [self.grid[row][col] for row in range(3)]
            if len(set(column_values)) == 1:  # Check if all three numbers in the column are the same
                return False
        # Check main diagonal for duplicates and ensure no same number in all three cells
        if len(set(self.grid[i][i] for i in range(3))) == 1:  # Check if all three numbers in the diagonal are the same
            return False
        # Check anti-diagonal for duplicates and ensure no same number in all three cells
        if len(set(self.grid[i][2 - i] for i in range(3))) == 1:  # Check if all three numbers in the anti-diagonal are the same
            return False
        return True
    def count_disappointments(self):
        disappointment_count = 0
        # Flatten the grid into a single list of numbers
        flat_grid = [num for row in self.grid for num in row]
        # Use a set to track unique permutations
        unique_permutations = set(itertools.permutations(flat_grid))
        for perm in unique_permutations:
            # Reconstruct the 3x3 grid from the permutation
            perm_grid = [list(perm[i:i + 3]) for i in range(0, 9, 3)]
            # Check rows for disappointment
            for row in perm_grid:
                if row[0] == row[1] and row[0] != row[2]:
                    disappointment_count += 1
            # Check columns for disappointment
            for col in range(3):
                if perm_grid[0][col] == perm_grid[1][col] and perm_grid[0][col] != perm_grid[2][col]:
                    disappointment_count += 1
            # Check main diagonal for disappointment
            if perm_grid[0][0] == perm_grid[1][1] and perm_grid[0][0] != perm_grid[2][2]:
                disappointment_count += 1
            # Check anti-diagonal for disappointment
            if perm_grid[2][0] == perm_grid[1][1] and perm_grid[2][0] != perm_grid[0][2]:
                disappointment_count += 1
        return disappointment_count