'''
This module contains the logic for the Gomoku game.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.winner = None
    def make_move(self, row, col):
        if self.winner is not None:
            return "Game has already ended."  # Prevent moves if the game has already ended
        if 0 <= row < 15 and 0 <= col < 15:  # Ensure the move is within bounds
            if self.board[row][col] is None:
                self.board[row][col] = self.current_player
                if self.check_winner():
                    self.winner = self.current_player
                self.current_player = "O" if self.current_player == "X" else "X"
                return "Move made."
            else:
                return "Invalid move. Cell already occupied."
        else:
            return "Invalid move. Please enter row and column between 0 and 14."
    def check_winner(self):
        # Check all possible winning conditions
        for row in range(15):
            for col in range(15):
                if self.board[row][col] is not None:
                    if self.check_direction(row, col, 1, 0) or \
                       self.check_direction(row, col, 0, 1) or \
                       self.check_direction(row, col, 1, 1) or \
                       self.check_direction(row, col, 1, -1):
                        self.winner = self.board[row][col]  # Set the winner
                        return True
        # Check for a draw
        if all(cell is not None for row in self.board for cell in row) and self.winner is None:
            self.winner = "Draw"
        return False
    def check_direction(self, row, col, delta_row, delta_col):
        count = 0
        for i in range(5):
            r = row + i * delta_row
            c = col + i * delta_col
            # Ensure we don't go out of bounds
            if 0 <= r < 15 and 0 <= c < 15 and self.board[r][c] == self.board[row][col]:
                count += 1
            else:
                break
        return count == 5
    def reset_game(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.winner = None
    def print_board(self):
        for row in self.board:
            print(' '.join(['.' if cell is None else cell for cell in row]))