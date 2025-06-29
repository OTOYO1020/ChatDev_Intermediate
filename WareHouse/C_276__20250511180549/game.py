'''
Contains the logic for the Gomoku game.
'''
class GomokuGame:
    def __init__(self):
        self.board_size = 15
        self.board = [[0] * self.board_size for _ in range(self.board_size)]
        self.current_player = 1
        self.winner = None
    def make_move(self, x, y):
        if 0 <= x < self.board_size and 0 <= y < self.board_size and self.board[x][y] == 0 and self.winner is None:
            self.board[x][y] = self.current_player
            if self.check_win(x, y):
                self.winner = self.current_player
            self.current_player = 3 - self.current_player  # Switch player
            return True
        return False
    def check_win(self, x, y):
        return (self.check_direction(x, y, 1, 0) or  # Horizontal
                self.check_direction(x, y, 0, 1) or  # Vertical
                self.check_direction(x, y, 1, 1) or  # Diagonal \
                self.check_direction(x, y, 1, -1))   # Diagonal /
    def check_direction(self, x, y, dx, dy):
        count = 0
        for step in range(-4, 5):
            nx, ny = x + step * dx, y + step * dy
            if 0 <= nx < self.board_size and 0 <= ny < self.board_size and self.board[nx][ny] == self.current_player:
                count += 1
                if count == 5:
                    return True
            else:
                count = 0
        return False
    def reset_game(self):
        self.board = [[0] * self.board_size for _ in range(self.board_size)]
        self.current_player = 1
        self.winner = None
    def is_draw(self):
        return all(cell != 0 for row in self.board for cell in row) and self.winner is None
    def __str__(self):
        display = ""
        for row in self.board:
            display += " ".join(['.' if cell == 0 else 'X' if cell == 1 else 'O' for cell in row]) + "\n"
        return display