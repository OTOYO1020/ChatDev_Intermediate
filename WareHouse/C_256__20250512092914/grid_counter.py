'''
Contains the logic for counting valid grid configurations.
'''
class GridCounter:
    '''
    Class to count valid configurations of a 3x3 grid.
    '''
    def validate_input(self, h1, h2, h3, w1, w2, w3):
        '''
        Validate that all inputs are within the range [3, 30].
        '''
        return all(3 <= x <= 30 for x in [h1, h2, h3, w1, w2, w3])
    def countWays(self, h1: int, h2: int, h3: int, w1: int, w2: int, w3: int) -> int:
        '''
        Count the number of valid configurations for the grid.
        '''
        if not self.validate_input(h1, h2, h3, w1, w2, w3):
            return 0
        grid = [[0] * 3 for _ in range(3)]
        col_sums = [0, 0, 0]  # Initialize column sums
        return self._count_configurations(grid, 0, h1, h2, h3, w1, w2, w3, col_sums)
    def _count_configurations(self, grid, row, h1, h2, h3, w1, w2, w3, col_sums):
        '''
        Recursive function to fill the grid and count valid configurations.
        '''
        if row == 3:
            # Check if the current grid configuration meets the row and column sums
            if (sum(grid[0]) == h1 and sum(grid[1]) == h2 and sum(grid[2]) == h3 and
                col_sums[0] == w1 and col_sums[1] == w2 and col_sums[2] == w3):
                return 1
            return 0
        count = 0
        remaining_row_sum = [h1, h2, h3][row]
        # Iterate through possible values for the current row
        for i in range(1, min(remaining_row_sum, 30) + 1):
            for j in range(1, min(remaining_row_sum - i, 30) + 1):
                k = remaining_row_sum - i - j
                if k < 1 or k > 30:
                    continue  # Skip invalid values
                # Check if adding these values would exceed column sums
                if (col_sums[0] + i > w1 or col_sums[1] + j > w2 or col_sums[2] + k > w3):
                    continue  # Skip invalid configurations
                grid[row] = [i, j, k]
                new_col_sums = col_sums[:]
                new_col_sums[0] += i
                new_col_sums[1] += j
                new_col_sums[2] += k
                # Proceed to the next row
                count += self._count_configurations(grid, row + 1, h1, h2, h3, w1, w2, w3, new_col_sums)
        return count