'''
Represents a single cell on the Gomoku board.
'''
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.value = ""  # Empty cell