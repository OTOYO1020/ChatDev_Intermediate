'''
This file contains the logic for the Gomoku game, including board management and win conditions.
'''
class GomokuLogic:
    def __init__(self, size):
        """
        Initializes the Gomoku game logic with a specified board size.
        Parameters:
        size (int): The size of the board (number of rows and columns).
        """
        self.size = size
        self.board = [['' for _ in range(size)] for _ in range(size)]
    def make_move(self, x, y, player):
        """
        Attempts to place the player's mark on the board at the specified coordinates.
        Parameters:
        x (int): The x-coordinate on the board (column).
        y (int): The y-coordinate on the board (row).
        player (str): The player's mark ('X' or 'O').
        Returns:
        bool: True if the move was successful, False if the cell was already occupied.
        """
        if self.board[y][x] == '':
            self.board[y][x] = player
            return True
        return False
    def is_winner(self, player):
        """
        Checks if the specified player has won the game.
        Parameters:
        player (str): The player's mark ('X' or 'O').
        Returns:
        bool: True if the player has won, False otherwise.
        """
        # Check horizontal, vertical, and diagonal lines for a win
        for y in range(self.size):
            for x in range(self.size):
                if self.check_line(x, y, 1, 0, player) or \
                   self.check_line(x, y, 0, 1, player) or \
                   self.check_line(x, y, 1, 1, player) or \
                   self.check_line(x, y, 1, -1, player):
                    return True
        return False
    def check_line(self, x, y, dx, dy, player):
        """
        Checks a line of five cells in the specified direction for a win.
        Parameters:
        x (int): The starting x-coordinate.
        y (int): The starting y-coordinate.
        dx (int): The change in x for each step (direction).
        dy (int): The change in y for each step (direction).
        player (str): The player's mark ('X' or 'O').
        Returns:
        bool: True if there are five in a row for the player, False otherwise.
        """
        count = 0
        for i in range(5):
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < self.size and 0 <= ny < self.size and self.board[ny][nx] == player:
                count += 1
            else:
                break
        return count == 5
    def is_draw(self):
        """
        Checks if the game is a draw.
        Returns:
        bool: True if the game is a draw, False otherwise.
        """
        # A draw occurs only if the board is full and there is no winner
        return all(cell != '' for row in self.board for cell in row) and not self.is_winner('X') and not self.is_winner('O')