'''
Contains the logic for the Gomoku game.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.winner = None
    def make_move(self, row, col):
        """
        Places the current player's mark on the board at the specified row and column.
        Parameters:
            row (int): The row index for the move (0-14).
            col (int): The column index for the move (0-14).
        Returns:
            None
        Raises:
            ValueError: If the move is invalid (out of bounds or cell already occupied).
        """
        if self.winner or self.is_draw():
            raise ValueError("Game over. No more moves can be made.")
        if not (0 <= row < 15 and 0 <= col < 15):
            raise ValueError("Invalid move. Row and column must be between 0 and 14.")
        if self.board[row][col] != ' ':
            raise ValueError("Invalid move. The cell is already occupied.")
        self.board[row][col] = self.current_player
        if self.check_winner(row, col):
            self.winner = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    def check_winner(self, row, col):
        """
        Checks if the current player has won the game after making a move.
        Parameters:
            row (int): The row index of the last move.
            col (int): The column index of the last move.
        Returns:
            bool: True if the current player has won, False otherwise.
        """
        return (self.check_line(row, col, 1, 0) or  # Horizontal
                self.check_line(row, col, 0, 1) or  # Vertical
                self.check_line(row, col, 1, 1) or  # Diagonal \
                self.check_line(row, col, 1, -1))   # Diagonal /
    def check_line(self, row, col, delta_row, delta_col):
        """
        Checks for a winning line in the specified direction.
        Parameters:
            row (int): The starting row index.
            col (int): The starting column index.
            delta_row (int): The change in row index for each step.
            delta_col (int): The change in column index for each step.
        Returns:
            bool: True if there are 5 consecutive marks, False otherwise.
        """
        count = 0
        for direction in [1, -1]:
            r, c = row, col
            while 0 <= r < 15 and 0 <= c < 15 and self.board[r][c] == self.current_player:
                count += 1
                r += direction * delta_row
                c += direction * delta_col
        return count >= 5
    def reset_game(self):
        """
        Resets the game board and current player to start a new game.
        Returns:
            None
        """
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.winner = None
    def display_board(self):
        """
        Displays the current state of the game board.
        Returns:
            None
        """
        for row in self.board:
            print('|'.join(row))
            print('-' * 29)
    def is_draw(self):
        """
        Checks if the game is a draw (no empty spaces left).
        Returns:
            bool: True if the game is a draw, False otherwise.
        """
        return all(cell != ' ' for row in self.board for cell in row) and self.winner is None
    def is_game_over(self):
        """
        Checks if the game is over (either a win or a draw).
        Returns:
            bool: True if the game is over, False otherwise.
        """
        return self.winner is not None or self.is_draw()