'''
Module for the Sheet class representing individual sheets.
'''
class Sheet:
    def __init__(self, height, width, representation):
        self.height = height
        self.width = width
        self.grid = self.create_grid(representation)
    def create_grid(self, representation):
        # Initialize the grid with transparent squares ('0')
        grid = [['0' for _ in range(self.width)] for _ in range(self.height)]
        # Fill the grid with the representation
        for i, row in enumerate(representation.split(';')):
            if i < self.height:  # Ensure we do not exceed the height
                for j, char in enumerate(row):
                    if j < self.width:  # Ensure we do not exceed the width
                        grid[i][j] = char
        return grid
    def can_fit(self, start_row, start_col, other_grid):
        '''
        Check if the sheet can fit within the grid starting from a specific row and column
        without overlapping with the already occupied positions in other_grid.
        '''
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == '1':  # Assuming '1' represents a black square
                    if start_row + i >= len(other_grid) or start_col + j >= len(other_grid[0]):
                        return False
                    if other_grid[start_row + i][start_col + j] == '1':  # Check for overlap
                        return False
        return True
    def paste(self, other_sheet, start_row, start_col):
        '''
        Paste another sheet onto this sheet at the specified position.
        '''
        for i in range(other_sheet.height):
            for j in range(other_sheet.width):
                if other_sheet.grid[i][j] == '1':  # Assuming '1' represents a black square
                    if 0 <= start_row + i < self.height and 0 <= start_col + j < self.width:
                        self.grid[start_row + i][start_col + j] = '1'
    def matches(self, other_sheet):
        '''
        Check if the black squares of this sheet match the black squares of another sheet.
        Transparent squares are ignored in the comparison.
        '''
        if self.height != other_sheet.height or self.width != other_sheet.width:
            return False  # Return False if dimensions do not match
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == '1' and other_sheet.grid[i][j] != '1':
                    return False
        return True