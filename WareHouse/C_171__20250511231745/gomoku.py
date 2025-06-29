'''
This module contains the GomokuGame class which handles the game logic.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.winner = None
    def make_move(self, row, col):
        if self.winner:
            return "Game over. Player {} has already won.".format(self.winner)
        if not (0 <= row < 15 and 0 <= col < 15):
            return "Invalid move. Please choose a row and column between 0 and 14."
        if self.board[row][col] is None:
            self.board[row][col] = self.current_player
            if self.check_winner(row, col):
                self.winner = self.current_player
                return f"Player {self.current_player} wins! Game over."
            self.current_player = "O" if self.current_player == "X" else "X"
        else:
            return "Invalid move. Cell already occupied."
        return None
    def check_winner(self, row, col):
        return (self.check_direction(row, col, 1, 0) or  # Horizontal
                self.check_direction(row, col, 0, 1) or  # Vertical
                self.check_direction(row, col, 1, 1) or  # Diagonal \
                self.check_direction(row, col, 1, -1))   # Diagonal /
    def check_direction(self, row, col, delta_row, delta_col):
        count = 0
        for direction in [1, -1]:
            r, c = row, col
            while 0 <= r < 15 and 0 <= c < 15 and self.board[r][c] == self.current_player:
                count += 1
                r += direction * delta_row
                c += direction * delta_col
        return count >= 5
    def reset_game(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.winner = None
    def print_board(self):
        for row in self.board:
            print(" ".join(['.' if cell is None else cell for cell in row]))