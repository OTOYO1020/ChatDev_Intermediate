'''
Module that defines the Board class for the Gomoku game.
'''
class Board:
    def __init__(self):
        self.size = 15
        self.board = [["" for _ in range(self.size)] for _ in range(self.size)]
    def place_piece(self, row, col, player):
        if self.board[row][col] == "":
            self.board[row][col] = player
            return True
        return False
    def get_piece(self, row, col):
        return self.board[row][col]
    def is_full(self):
        for row in self.board:
            if "" in row:
                return False
        return True
    def reset(self):
        self.board = [["" for _ in range(self.size)] for _ in range(self.size)]
    def check_winner(self, row, col, player):
        return (self.check_direction(row, col, player, 1, 0) or  # Horizontal
                self.check_direction(row, col, player, 0, 1) or  # Vertical
                self.check_direction(row, col, player, 1, 1) or  # Diagonal \
                self.check_direction(row, col, player, 1, -1))   # Diagonal /
    def check_direction(self, row, col, player, delta_row, delta_col):
        count = 0
        for direction in [1, -1]:
            r, c = row, col
            while 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == player:
                count += 1
                r += direction * delta_row
                c += direction * delta_col
                # Check if we exceed the board boundaries
                if not (0 <= r < self.size and 0 <= c < self.size):
                    break
        return count >= 5  # Return true if there are 5 or more in a row