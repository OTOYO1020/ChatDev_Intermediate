'''
This module contains the GomokuGame class which handles the game logic.
'''
class GomokuGame:
    def __init__(self):
        self.board_size = 15
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'X'
        self.winner = None
    def make_move(self, x, y):
        if self.board[x][y] == ' ' and self.winner is None:
            self.board[x][y] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True  # Move was successful
        return False  # Move was not successful
    def check_winner(self):
        # Check horizontal, vertical, and diagonal lines for a win
        for x in range(self.board_size):
            for y in range(self.board_size):
                if self.board[x][y] != ' ':
                    if self.check_line(x, y, 1, 0) or self.check_line(x, y, 0, 1) or \
                       self.check_line(x, y, 1, 1) or self.check_line(x, y, 1, -1):
                        return True
        return False
    def check_line(self, x, y, dx, dy):
        count = 0
        # Check in the positive direction
        for i in range(5):
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < self.board_size and 0 <= ny < self.board_size and self.board[nx][ny] == self.board[x][y]:
                count += 1
            else:
                break
        # Check in the negative direction
        for i in range(1, 5):
            nx, ny = x - i * dx, y - i * dy
            if 0 <= nx < self.board_size and 0 <= ny < self.board_size and self.board[nx][ny] == self.board[x][y]:
                count += 1
            else:
                break
        return count >= 5  # Return true if there are 5 or more in a row
    def reset_game(self):
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'X'
        self.winner = None
    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * (self.board_size * 2 - 1))