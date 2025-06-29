'''
This module contains the Gomoku game logic without GUI implementation.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.winner = None
    def make_move(self, row, col):
        """
        Places the current player's mark on the board at the specified row and column.
        Checks for a winner after the move is made.
        """
        if self.winner is not None:
            print("Game over! Player {} has already won.".format(self.winner))
            return  # Prevent further moves if the game is already won
        if self.is_full():
            print("Game over! The board is full, it's a draw.")
            return  # Prevent further moves if the board is full
        if not (0 <= row < 15 and 0 <= col < 15):
            print("Move out of bounds. Please enter values between 0 and 14.")
            return  # Early return if the move is out of bounds
        if self.board[row][col] is not None:
            print("Cell already occupied. Please choose another cell.")
            return  # Inform the player that the cell is already taken
        self.board[row][col] = self.current_player
        if self.check_winner(row, col):
            self.winner = self.current_player
            print(f"Player {self.winner} wins!")  # Inform the players of the win
        else:
            self.current_player = "O" if self.current_player == "X" else "X"
    def check_winner(self, row, col):
        """
        Checks if the current player has won the game by checking all directions.
        """
        return (self.check_direction(row, col, 1, 0) or  # Horizontal
                self.check_direction(row, col, 0, 1) or  # Vertical
                self.check_direction(row, col, 1, 1) or  # Diagonal \
                self.check_direction(row, col, 1, -1))   # Diagonal /
    def check_direction(self, row, col, delta_row, delta_col):
        """
        Checks in a specific direction for a winning condition.
        Counts consecutive marks of the current player.
        """
        count = 0
        for direction in [1, -1]:
            r, c = row, col
            while 0 <= r < 15 and 0 <= c < 15 and self.board[r][c] == self.current_player:
                count += 1
                r += delta_row * direction
                c += delta_col * direction
        return count >= 5
    def reset_game(self):
        """
        Resets the game board and current player to start a new game.
        """
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.winner = None
    def print_board(self):
        """
        Prints the current state of the game board to the console.
        """
        for row in self.board:
            print(" ".join(['.' if cell is None else cell for cell in row]))
    def is_full(self):
        """
        Checks if the board is full, indicating a draw.
        """
        return all(cell is not None for row in self.board for cell in row)