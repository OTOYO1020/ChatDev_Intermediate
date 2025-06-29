'''
This module contains the GomokuGame class which manages the game logic.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.winner = None
    def reset_game(self):
        '''Resets the game board and current player.'''
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.winner = None
    def make_move(self, row, col):
        '''Attempts to make a move on the board.'''
        if self.winner is not None:
            return "Game over. Please start a new game."
        if not (0 <= row < 15 and 0 <= col < 15):
            return "Move out of bounds. Please enter values between 0 and 14."
        if self.board[row][col] is not None:
            return "Cell already occupied. Please choose another cell."
        self.board[row][col] = self.current_player
        if self.check_win(row, col):
            self.winner = self.current_player
        self.current_player = "O" if self.current_player == "X" else "X"
        return True  # Move was successful
    def check_win(self, row, col):
        '''Checks if the current player has won the game.'''
        return (self.check_line(row, col, 1, 0) or  # Horizontal
                self.check_line(row, col, 0, 1) or  # Vertical
                self.check_line(row, col, 1, 1) or  # Diagonal \
                self.check_line(row, col, 1, -1))   # Diagonal /
    def check_line(self, row, col, delta_row, delta_col):
        '''Checks for a winning line in a specified direction.'''
        count = 0
        for direction in [1, -1]:
            r, c = row, col
            while 0 <= r < 15 and 0 <= c < 15 and self.board[r][c] == self.current_player:
                count += 1
                r += direction * delta_row
                c += direction * delta_col
        return count >= 5
    def print_board(self):
        '''Prints the current state of the game board.'''
        for row in self.board:
            print(' '.join(['.' if cell is None else cell for cell in row]))
    def is_board_full(self):
        '''Checks if the board is full.'''
        return all(cell is not None for row in self.board for cell in row)