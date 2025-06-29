'''
Class to represent the Gomoku game board and handle game logic.
'''
class Board:
    def __init__(self, game):
        self.game = game
        self.size = 15
        self.grid = [[None for _ in range(self.size)] for _ in range(self.size)]
    def display_board(self):
        # Display the current state of the board
        for row in self.grid:
            print(' '.join(['.' if cell is None else cell[0] for cell in row]))
    def place_piece(self, x, y, color):
        # Place a piece on the board if the cell is empty
        if self.grid[x][y] is None:
            self.grid[x][y] = color
            return True
        return False  # Return False if the cell is occupied
    def check_win(self, color):
        # Check for a win condition in all directions
        for x in range(self.size):
            for y in range(self.size):
                if self.grid[x][y] == color:
                    if self.check_direction(x, y, color, 1, 0) or \
                       self.check_direction(x, y, color, 0, 1) or \
                       self.check_direction(x, y, color, 1, 1) or \
                       self.check_direction(x, y, color, 1, -1):
                        return True
        return False
    def check_direction(self, x, y, color, dx, dy):
        count = 0
        # Count pieces in the specified direction
        for step in range(5):  # Check for up to 5 pieces in the positive direction
            nx, ny = x + step * dx, y + step * dy
            if 0 <= nx < self.size and 0 <= ny < self.size and self.grid[nx][ny] == color:
                count += 1
            else:
                break
        # Count pieces in the opposite direction
        for step in range(1, 5):  # Check for up to 5 pieces in the negative direction
            nx, ny = x - step * dx, y - step * dy
            if 0 <= nx < self.size and 0 <= ny < self.size and self.grid[nx][ny] == color:
                count += 1
            else:
                break
        return count >= 5  # Check for 5 or more pieces