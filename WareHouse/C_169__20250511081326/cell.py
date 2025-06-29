'''
Contains the Cell class to represent each cell on the Gomoku board.
'''
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None  # None means the cell is empty