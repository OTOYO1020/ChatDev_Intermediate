'''
This module contains the GomokuGame class which manages the game state,
including the board, player turns, and win conditions.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.game_over = False  # New attribute to track game state
    def make_move(self, x, y):
        if not (0 <= x < 15 and 0 <= y < 15):  # Check if coordinates are within bounds
            return "Invalid move. Coordinates must be between 0 and 14."
        if self.board[x][y] is None and not self.game_over:  # Check if game is over
            self.board[x][y] = self.current_player
            if self.check_win():
                self.game_over = True  # Set game over when a player wins
                return f'Player {self.current_player} wins!'
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        return None
    def check_win(self):
        # Check horizontal, vertical, and diagonal for a win
        for x in range(15):
            for y in range(15):
                if self.board[x][y] is not None:
                    if self.check_direction(x, y, 1, 0) or \
                       self.check_direction(x, y, 0, 1) or \
                       self.check_direction(x, y, 1, 1) or \
                       self.check_direction(x, y, 1, -1):
                        return True
        return False
    def check_direction(self, x, y, dx, dy):
        count = 0
        for i in range(5):
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < 15 and 0 <= ny < 15 and self.board[nx][ny] == self.board[x][y]:
                count += 1
            else:
                break
        return count == 5
    def reset_game(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.game_over = False  # Reset game state
    def display_board(self):
        for row in self.board:
            print(' '.join(['.' if cell is None else cell for cell in row]))
        print()