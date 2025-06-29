'''
Contains the game logic for the Gomoku game.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[0 for _ in range(15)] for _ in range(15)]
        self.current_player = 1
        self.game_over = False
    def make_move(self, x, y):
        if self.game_over:
            print("Game is already over. Please reset to play again.")
            return False  # Prevent further moves if the game is over
        if self.board[x][y] == 0:
            self.board[x][y] = self.current_player
            if self.check_win(x, y):
                self.game_over = True
            self.current_player = 3 - self.current_player  # Switch between player 1 and 2
            return True  # Move was successful
        else:
            return False  # Move was not successful (cell already occupied)
    def check_win(self, x, y):
        # Check horizontal, vertical, and diagonal lines for a win
        return (self.check_direction(x, y, 1, 0) or  # Horizontal
                self.check_direction(x, y, 0, 1) or  # Vertical
                self.check_direction(x, y, 1, 1) or  # Diagonal \
                self.check_direction(x, y, 1, -1))   # Diagonal /
    def check_direction(self, x, y, dx, dy):
        count = 0
        for step in range(-4, 5):
            nx, ny = x + step * dx, y + step * dy
            # Check if the new coordinates are within the bounds of the board
            if 0 <= nx < 15 and 0 <= ny < 15 and self.board[nx][ny] == self.current_player:
                count += 1
                if count == 5:
                    return True
            else:
                count = 0  # Reset count if out of bounds or not the current player's piece
        return False
    def reset_game(self):
        self.board = [[0 for _ in range(15)] for _ in range(15)]
        self.current_player = 1
        self.game_over = False
    def __str__(self):
        display = ""
        for row in self.board:
            display += ' '.join(['.' if cell == 0 else 'X' if cell == 1 else 'O' for cell in row]) + "\n"
        return display