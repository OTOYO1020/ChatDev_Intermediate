'''
This module contains the GomokuGame class, which handles the game logic for Gomoku.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.game_over = False
    def make_move(self, row, col):
        if self.board[row][col] == ' ' and not self.game_over:
            self.board[row][col] = self.current_player
            if self.check_win():  # Check win condition for the current player
                self.game_over = True
                return  # Exit the method if the game is over
            self.current_player = 'O' if self.current_player == 'X' else 'X'
    def check_win(self):
        # Check horizontal, vertical, and diagonal for a win
        for row in range(15):
            for col in range(15):
                if self.board[row][col] != ' ':
                    if self.check_direction(row, col, 1, 0) or \
                       self.check_direction(row, col, 0, 1) or \
                       self.check_direction(row, col, 1, 1) or \
                       self.check_direction(row, col, 1, -1):
                        return True
        return False
    def check_direction(self, row, col, delta_row, delta_col):
        count = 0
        for i in range(5):
            r = row + i * delta_row
            c = col + i * delta_col
            if 0 <= r < 15 and 0 <= c < 15 and self.board[r][c] == self.current_player:
                count += 1
            else:
                break
        return count == 5
    def reset_game(self):
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.game_over = False
    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 29)