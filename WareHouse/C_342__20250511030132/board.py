'''
Contains the Board class that manages the game state and logic for Gomoku.
'''
class Board:
    def __init__(self, game):
        self.game = game
        self.reset()
    def reset(self):
        self.grid = [['' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.winner = None
    def place_piece(self, x, y):
        if self.winner is not None:
            print(f"Game over! Player {self.winner} has already won.")
            return False
        if self.grid[x][y] == '':
            self.grid[x][y] = self.current_player
            # Check for draw condition after placing the piece
            if all(cell != '' for row in self.grid for cell in row) and self.winner is None:
                self.winner = 'Draw'
                return True
            # Check for a winner after placing the piece
            if self.check_winner():
                return True
            # Switch player after checking for a winner
            self.switch_player()
            return True
        else:
            print(f"Cell ({x}, {y}) is already occupied. Please choose another cell.")
            return False
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    def check_winner(self):
        # Check horizontal, vertical, and diagonal for a win
        for i in range(15):
            for j in range(15):
                if self.grid[i][j] != '':
                    if self.check_direction(i, j, 1, 0) or \
                       self.check_direction(i, j, 0, 1) or \
                       self.check_direction(i, j, 1, 1) or \
                       self.check_direction(i, j, 1, -1):
                        self.winner = self.grid[i][j]
                        return True
        return False
    def check_direction(self, x, y, dx, dy):
        '''
        Check for five in a row in a specified direction.
        Parameters:
        x (int): The starting row index.
        y (int): The starting column index.
        dx (int): The change in row index (direction).
        dy (int): The change in column index (direction).
        Returns:
        bool: True if there are five pieces in a row, False otherwise.
        '''
        count = 1  # Start with 1 to count the initial piece
        for step in range(1, 5):  # Start from 1 to check the next 4 pieces
            nx, ny = x + step * dx, y + step * dy
            if 0 <= nx < 15 and 0 <= ny < 15 and self.grid[nx][ny] == self.grid[x][y]:
                count += 1
            else:
                break
        return count == 5