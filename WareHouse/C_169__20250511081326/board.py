'''
Contains the Board class to manage the game state and board representation.
'''
from cell import Cell
class Board:
    def __init__(self):
        self.size = 15
        self.cells = [[Cell(x, y) for y in range(self.size)] for x in range(self.size)]
    def display(self):
        for row in self.cells:
            print(" ".join(cell.value if cell.value else '.' for cell in row))
        print()
    def make_move(self, x, y, player):
        '''
        Makes a move on the board for the given player.
        Returns True if the move was successful, False otherwise.
        '''
        if 0 <= x < self.size and 0 <= y < self.size and self.cells[x][y].value is None:
            self.cells[x][y].value = player
            return True
        return False
    def check_winner(self):
        '''
        Checks if there is a winner.
        Returns True if there is a winner, False otherwise.
        '''
        for i in range(self.size):
            for j in range(self.size):
                if self.cells[i][j].value and (self.check_direction(i, j, 1, 0) or
                                                self.check_direction(i, j, 0, 1) or
                                                self.check_direction(i, j, 1, 1) or
                                                self.check_direction(i, j, 1, -1)):
                    return True
        return False  # Only return True if a winner is found
    def check_direction(self, x, y, dx, dy):
        '''
        Checks for a sequence of exactly 5 in a given direction.
        Returns True if there are exactly 5 in a row, False otherwise.
        '''
        count = 0
        # Count in the positive direction
        for step in range(5):
            nx, ny = x + step * dx, y + step * dy
            if 0 <= nx < self.size and 0 <= ny < self.size and self.cells[nx][ny].value == self.cells[x][y].value:
                count += 1
            else:
                break
        # Check in the negative direction
        for step in range(1, 5):
            nx, ny = x - step * dx, y - step * dy
            if 0 <= nx < self.size and 0 <= ny < self.size and self.cells[nx][ny].value == self.cells[x][y].value:
                count += 1
            else:
                break
        # Ensure there are exactly 5 in a row
        return count == 5
    def is_draw(self):
        '''
        Checks if the game is a draw.
        Returns True if the game is a draw, False otherwise.
        '''
        return all(cell.value is not None for row in self.cells for cell in row)