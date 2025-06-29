'''
This module contains the logic for the Gomoku game.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.winner = None
    def make_move(self, row, col):
        if self.board[row][col] != ' ':
            print("Invalid move. The cell is already occupied.")
            return
        if self.winner is not None:
            print("Invalid move. The game has already been won.")
            return
        self.board[row][col] = self.current_player
        if self.check_winner(row, col):
            self.winner = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    def check_winner(self, row, col):
        return (self.check_line(row, col, 1, 0) or  # Horizontal
                self.check_line(row, col, 0, 1) or  # Vertical
                self.check_line(row, col, 1, 1) or  # Diagonal \
                self.check_line(row, col, 1, -1))   # Diagonal /
    def check_line(self, row, col, delta_row, delta_col):
        count = 1  # Start with the current piece
        for direction in [1, -1]:  # Check both directions
            step = 1
            while True:
                r = row + step * delta_row * direction
                c = col + step * delta_col * direction
                if 0 <= r < 15 and 0 <= c < 15 and self.board[r][c] == self.current_player:
                    count += 1
                    step += 1
                else:
                    break
        return count >= 5
    def reset_game(self):
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.winner = None
    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 29)