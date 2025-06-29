'''
This module contains the logic for the Gomoku game.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.winner = None
    def make_move(self, row, col):
        if not (0 <= row < 15 and 0 <= col < 15):
            print("Invalid move: Out of bounds.")
            return False  # Indicate that the move was not successful
        if self.board[row][col] != ' ':
            print("Invalid move: Cell already occupied.")
            return False  # Indicate that the move was not successful
        if self.winner is None:
            self.board[row][col] = self.current_player
            if self.check_winner(row, col):
                self.winner = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True  # Indicate that the move was successful
        return False  # Indicate that the move was not successful
    def check_winner(self, row, col):
        # Check horizontal, vertical, and diagonal lines for a win
        return (self.check_line(row, col, 1, 0) or  # Horizontal
                self.check_line(row, col, 0, 1) or  # Vertical
                self.check_line(row, col, 1, 1) or  # Diagonal \
                self.check_line(row, col, 1, -1))   # Diagonal /
    def check_line(self, row, col, delta_row, delta_col):
        count = 0
        for direction in (1, -1):
            r, c = row, col
            while 0 <= r < 15 and 0 <= c < 15 and self.board[r][c] == self.current_player:
                count += 1
                r += direction * delta_row
                c += direction * delta_col
        return count >= 5
    def reset_game(self):
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.winner = None