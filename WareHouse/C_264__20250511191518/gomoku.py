'''
This module contains the logic for the Gomoku game, including board management,
player turns, and win condition checks.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.winner = None
    def make_move(self, row, col):
        if self.board[row][col] is None and self.winner is None:
            self.board[row][col] = self.current_player
            if self.check_winner(row, col):
                self.winner = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
    def check_winner(self, row, col):
        return (self.check_line(row, col, 1, 0) or  # Horizontal
                self.check_line(row, col, 0, 1) or  # Vertical
                self.check_line(row, col, 1, 1) or  # Diagonal \
                self.check_line(row, col, 1, -1))   # Diagonal /
    def check_line(self, row, col, delta_row, delta_col):
        count = 0
        for direction in [1, -1]:
            r, c = row, col
            while 0 <= r < 15 and 0 <= c < 15 and self.board[r][c] == self.board[row][col]:
                count += 1
                if count == 5:
                    return True
                r += direction * delta_row
                c += direction * delta_col
        return False
    def reset_game(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.winner = None
    def print_board(self):
        for row in self.board:
            print(" ".join(['.' if cell is None else cell for cell in row]))