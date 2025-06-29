'''
Contains the Board class that manages the game board and game logic.
'''
class Board:
    def __init__(self):
        self.size = 15
        self.board = [["" for _ in range(self.size)] for _ in range(self.size)]
    def display_board(self):
        """Display the current state of the board."""
        for row in self.board:
            print(" | ".join([cell if cell else "." for cell in row]))
            print("-" * (self.size * 4 - 1))
    def place_piece(self, row, col, symbol):
        """Place a piece on the board if the cell is empty.
        Parameters:
        row (int): The row index for the piece.
        col (int): The column index for the piece.
        symbol (str): The symbol of the player.
        Returns:
        bool: True if the piece was placed, False otherwise.
        """
        if self.board[row][col] == "":
            self.board[row][col] = symbol
            return True
        else:
            return False  # Return False if the cell is already occupied
    def check_winner(self, symbol):
        """Check if the specified symbol has won the game.
        Parameters:
        symbol (str): The symbol to check for a win.
        Returns:
        bool: True if the symbol has won, False otherwise.
        """
        # Check horizontal, vertical, and diagonal for a win
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == symbol:  # Only check if the cell is occupied
                    if self.check_direction(row, col, symbol):
                        return True
        return False
    def check_direction(self, row, col, symbol):
        """Check all directions for a win.
        Parameters:
        row (int): The starting row index.
        col (int): The starting column index.
        symbol (str): The symbol to check.
        Returns:
        bool: True if there is a winning line, False otherwise.
        """
        return (self.check_line(row, col, symbol, 1, 0) or  # Horizontal
                self.check_line(row, col, symbol, 0, 1) or  # Vertical
                self.check_line(row, col, symbol, 1, 1) or  # Diagonal \
                self.check_line(row, col, symbol, 1, -1)    # Diagonal /
               )
    def check_line(self, row, col, symbol, delta_row, delta_col):
        """Check a line in a specific direction for a win.
        Parameters:
        row (int): The starting row index.
        col (int): The starting column index.
        symbol (str): The symbol to check.
        delta_row (int): The change in row index for each step.
        delta_col (int): The change in column index for each step.
        Returns:
        bool: True if there are five in a row, False otherwise.
        """
        count = 0
        for i in range(5):
            r = row + i * delta_row
            c = col + i * delta_col
            # Check if the indices are within bounds before accessing the board
            if 0 <= r < self.size and 0 <= c < self.size:
                if self.board[r][c] == symbol:
                    count += 1
                else:
                    break
            else:
                break  # Stop checking if out of bounds
        return count == 5
    def is_full(self):
        """Check if the board is full.
        Returns:
        bool: True if the board is full, False otherwise.
        """
        for row in self.board:
            if "" in row:
                return False
        return True