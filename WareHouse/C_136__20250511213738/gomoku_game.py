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
            return False, "Game Over. No more moves can be made."  # Clear message for moves after game over
        if row < 0 or row >= 15 or col < 0 or col >= 15:
            return False, "Invalid move. Please choose a row and column between 0 and 14."  # Check for valid range
        if self.board[row][col] is None:
            self.board[row][col] = self.current_player
            if self.check_win(row, col):
                self.winner = self.current_player
                return True, "Game Over"  # Indicate game over
            self.current_player = "O" if self.current_player == "X" else "X"
            return True, None  # Move was successful
        else:
            return False, "Cell is already occupied. Please choose another cell."  # Move was invalid
    def check_win(self, row, col):
        # Check horizontal, vertical, and diagonal lines for a win
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            for d in [1, -1]:
                r, c = row, col
                while 0 <= r + d * dr < 15 and 0 <= c + d * dc < 15 and self.board[r + d * dr][c + d * dc] == self.current_player:
                    count += 1
                    r += d * dr
                    c += d * dc
            if count >= 5:
                return True
        return False
    def reset_game(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.winner = None
    def print_board(self):
        for row in self.board:
            print(' '.join(['.' if cell is None else cell for cell in row]))