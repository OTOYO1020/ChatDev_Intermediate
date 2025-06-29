'''
Represents a single cell on the Gomoku board.
'''
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = 0  # 0: empty, 1: player 1, 2: player 2