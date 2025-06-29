'''
This module contains the GomokuGame class which handles the game logic for Gomoku.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
    def make_move(self, x, y):
        if self.board[x][y] is not None:
            return "Invalid move. Cell is already occupied."
        self.board[x][y] = self.current_player
        if self.check_win():
            return f'Player {self.current_player} wins!'
        if self.is_draw():
            return "The game is a draw!"
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return None
    def check_win(self):
        # Check horizontal, vertical, and diagonal lines for a win
        for x in range(15):
            for y in range(15):
                if self.board[x][y] is not None:
                    if (self.check_direction(x, y, 1, 0) or  # Horizontal
                        self.check_direction(x, y, 0, 1) or  # Vertical
                        self.check_direction(x, y, 1, 1) or  # Diagonal \
                        self.check_direction(x, y, 1, -1)):  # Diagonal /
                        return True
        return False
    def check_direction(self, x, y, dx, dy):
        count = 1  # Start with the current piece
        # Count in the positive direction
        for i in range(1, 5):
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < 15 and 0 <= ny < 15 and self.board[nx][ny] == self.board[x][y]:
                count += 1
            else:
                break
        # Count in the negative direction
        for i in range(1, 5):
            nx, ny = x - i * dx, y - i * dy
            if 0 <= nx < 15 and 0 <= ny < 15 and self.board[nx][ny] == self.board[x][y]:
                count += 1
            else:
                break
        # Check if the count is at least 5
        return count >= 5  # Return True if there are at least 5 in a row
    def is_draw(self):
        return all(cell is not None for row in self.board for cell in row)
    def reset_game(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
    def print_board(self):
        for row in self.board:
            print(' '.join(['.' if cell is None else cell for cell in row]))