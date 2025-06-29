'''
Module to define the Grid class for the color grid.
'''
class Grid:
    def __init__(self, size, colors):
        self.size = size
        self.colors = colors
        self.grid = self.initialize_grid()
    def initialize_grid(self):
        return [[self.colors[i][j] for j in range(self.size)] for i in range(self.size)]
    def count_black_squares(self, query):
        '''
        Count the number of black squares in the specified rectangular area defined by the query.
        '''
        black_count = 0
        # Adjusting for 1-based to 0-based index
        for i in range(query.A - 1, query.C):  # Adjust A and C
            for j in range(query.B - 1, query.D):  # Adjust B and D
                # Directly access the grid without modulo
                if self.grid[i][j] == 'B':
                    black_count += 1
        return black_count