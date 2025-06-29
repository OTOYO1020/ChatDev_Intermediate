'''
Module to define the Grid class for managing the grid of squares.
'''
class Grid:
    def __init__(self, size, grid_input):
        self.size = size
        self.grid = [list(row) for row in grid_input]
        self.white_squares = self.get_white_squares()
    def get_white_squares(self):
        return [(i, j) for i in range(self.size) for j in range(self.size) if self.grid[i][j] == '.']