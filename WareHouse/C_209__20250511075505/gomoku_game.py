'''
This module contains the logic for the Gomoku game.
'''
class GomokuGame:
    def __init__(self):
        self.board_size = 15
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'X'
        self.winner = None
    def make_move(self, x, y):
        if self.winner is not None:
            raise Exception("Game is already over. Please reset the game to play again.")
        if not (0 <= x < self.board_size and 0 <= y < self.board_size):  # Bounds checking
            raise Exception("Invalid move. Please enter numbers between 0 and 14.")
        if self.board[x][y] == ' ':
            self.board[x][y] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
        else:
            raise Exception("Invalid move. The cell is already occupied.")
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    def check_winner(self):
        # Check horizontal, vertical, and diagonal for a winner
        for x in range(self.board_size):
            for y in range(self.board_size):
                if self.board[x][y] != ' ':
                    if self.check_direction(x, y, 1, 0) or self.check_direction(x, y, 0, 1) or \
                       self.check_direction(x, y, 1, 1) or self.check_direction(x, y, 1, -1):
                        return True
        return False
    def check_direction(self, x, y, dx, dy):
        count = 1  # Start with the current piece
        # Check in the positive direction
        for i in range(1, 5):
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
        return count >= 5  # Return True if there are 5 or more in a row
    def reset_game(self):
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'X'
        self.winner = None