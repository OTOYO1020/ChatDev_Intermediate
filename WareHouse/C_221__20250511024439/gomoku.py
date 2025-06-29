'''
This module contains the GomokuGame class which handles the game logic.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.game_over = False  # Track if the game is over
    def make_move(self, x, y):
        if self.game_over:
            return "Game over! Please reset to play again."  # Inform player that the game is over
        if self.board[x][y] is not None:
            return "Invalid move! Cell already occupied."  # Inform player of invalid move
        self.board[x][y] = self.current_player
        if self.check_winner(x, y):
            self.game_over = True  # Set game over state
            return f'Player {self.current_player} wins!'
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return None
    def check_winner(self, x, y):
        # Check horizontal, vertical, and diagonal for a win
        return (self.check_direction(x, y, 1, 0) or  # Horizontal
                self.check_direction(x, y, 0, 1) or  # Vertical
                self.check_direction(x, y, 1, 1) or  # Diagonal \
                self.check_direction(x, y, 1, -1))   # Diagonal /
    def check_direction(self, x, y, dx, dy):
        count = 1  # Start with the current piece already counted
        # Check in the positive direction
        for step in range(1, 5):
            nx, ny = x + step * dx, y + step * dy
            if 0 <= nx < 15 and 0 <= ny < 15 and self.board[nx][ny] == self.current_player:
                count += 1
            else:
                break  # Stop if we hit an empty space or out of bounds
        # Check in the negative direction
        for step in range(1, 5):
            nx, ny = x - step * dx, y - step * dy
            if 0 <= nx < 15 and 0 <= ny < 15 and self.board[nx][ny] == self.current_player:
                count += 1
            else:
                break  # Stop if we hit an empty space or out of bounds
        return count >= 5  # Return True if we have 5 in a row
    def reset_game(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.game_over = False  # Reset game over state