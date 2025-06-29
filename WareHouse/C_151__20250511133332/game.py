'''
Contains the logic for the Gomoku game.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.game_over = False
    def make_move(self, x, y):
        if not (0 <= x < 15 and 0 <= y < 15):
            return "Invalid move. Coordinates must be between 0 and 14."
        if self.board[x][y] is None and not self.game_over:
            self.board[x][y] = self.current_player
            if self.check_winner(x, y):  # Pass the last move coordinates
                self.game_over = True
                return f"Player {self.current_player} wins!"
            self.current_player = "O" if self.current_player == "X" else "X"
        else:
            return "Invalid move. Cell is already occupied."  # New feedback for invalid move
        return None
    def check_winner(self, x, y):
        # Check the last move's position for a win
        return (self.check_direction(x, y, 1, 0) or  # Horizontal
                self.check_direction(x, y, 0, 1) or  # Vertical
                self.check_direction(x, y, 1, 1) or  # Diagonal \
                self.check_direction(x, y, 1, -1))   # Diagonal /
    def check_direction(self, x, y, dx, dy):
        count = 1  # Start with the current piece
        # Check in the positive direction
        for i in range(1, 5):
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < 15 and 0 <= ny < 15 and self.board[nx][ny] == self.board[x][y]:
                count += 1
            else:
                break
        # Check in the negative direction
        for i in range(1, 5):
            nx, ny = x - i * dx, y - i * dy
            if 0 <= nx < 15 and 0 <= ny < 15 and self.board[nx][ny] == self.board[x][y]:
                count += 1
            else:
                break
        return count >= 5  # Allow for 5 or more in a row
    def reset_game(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.game_over = False
    def display_board(self):
        for row in self.board:
            print(' '.join(['.' if cell is None else cell for cell in row]))