'''
This module contains the GomokuGame class which manages the game logic.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.game_over = False  # Flag to indicate if the game is over
    def make_move(self, x, y):
        if self.board[x][y] is None and not self.game_over:
            self.board[x][y] = self.current_player
            winner = self.check_winner()
            if winner:
                self.game_over = True  # Set game over flag
                return f"Player {winner} wins!"  # Use the winning player
            self.current_player = "O" if self.current_player == "X" else "X"
        return None
    def check_winner(self):
        # Check horizontal, vertical, and diagonal for a win
        for x in range(15):
            for y in range(15):
                if self.board[x][y] is not None:
                    if self.check_direction(x, y, 1, 0) or \
                       self.check_direction(x, y, 0, 1) or \
                       self.check_direction(x, y, 1, 1) or \
                       self.check_direction(x, y, 1, -1):
                        return self.board[x][y]  # Return the winning player
        return None
    def check_direction(self, x, y, dx, dy):
        count = 0
        for i in range(5):
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < 15 and 0 <= ny < 15 and self.board[nx][ny] == self.board[x][y]:
                count += 1
            else:
                break
        # Check if there are at least 5 pieces in a row
        if count >= 5:
            next_x, next_y = x + 5 * dx, y + 5 * dy
            if not (0 <= next_x < 15 and 0 <= next_y < 15) or self.board[next_x][next_y] != self.board[x][y]:
                return True
        return False
    def reset_game(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.game_over = False  # Reset game over flag
    def display_board(self):
        for row in self.board:
            print(" ".join(['.' if cell is None else cell for cell in row]))