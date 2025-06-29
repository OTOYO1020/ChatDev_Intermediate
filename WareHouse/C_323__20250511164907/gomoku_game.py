'''
This module contains the GomokuGame class that handles the game logic for Gomoku.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.game_over = False  # Add a game_over attribute
    def make_move(self, x, y):
        if self.game_over:  # Check if the game has already been won
            return "Game has already ended. Please reset to play again."
        if self.board[x][y] is None:
            self.board[x][y] = self.current_player
            if self.check_winner():
                self.game_over = True  # Set game_over to True
                return f"Player {self.current_player} wins!"
            self.current_player = "O" if self.current_player == "X" else "X"
        else:
            return "Invalid move. Cell already occupied."
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
                        return True
        return False
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
        return count >= 5  # Check for 5 or more
    def reset_game(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.game_over = False  # Reset game_over when the game resets
    def display_board(self):
        """Displays the current state of the board in the console."""
        for row in self.board:
            print(" ".join(['.' if cell is None else cell for cell in row]))
        print()