'''
Module containing the Grid class for grid operations.
'''
class Grid:
    '''
    Class representing a grid and its operations.
    '''
    def __init__(self, height, width):
        '''
        Initializes the grid dimensions.
        '''
        self.height = height
        self.width = width
        self.holed_squares = set()
    def add_hole(self, hole):
        '''
        Adds a single holed square to the grid, avoiding duplicates.
        '''
        if hole not in self.holed_squares:  # Check for duplicates
            self.holed_squares.add(hole)
    def count_holeless_squares(self):
        '''
        Counts the number of holeless squares in the grid.
        '''
        holeless_count = 0
        for i in range(self.height):
            for j in range(self.width):
                for n in range(1, min(self.height - i, self.width - j) + 1):
                    # Check if the square defined by (i, j) and size n is holeless
                    if self.is_holeless(i, j, n):
                        holeless_count += 1  # Increment count for each holeless square
        return holeless_count
    def is_holeless(self, x, y, size):
        '''
        Checks if the square defined by (x, y) and size is holeless.
        '''
        for i in range(x, x + size):
            for j in range(y, y + size):
                if (i, j) in self.holed_squares:
                    return False
        return True