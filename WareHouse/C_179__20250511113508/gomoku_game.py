'''
This module contains the logic for the Gomoku game.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
    def make_move(self, row, col):
        if self.board[row][col] is not None:
            return "Invalid move! Cell is already occupied."
        self.board[row][col] = self.current_player
        winner = self.check_winner()
        if winner:
            return f"Player {winner} wins!"  # Use the winning player's symbol
        if all(cell is not None for row in self.board for cell in row):
            return "It's a draw!"  # Check for draw condition
        self.current_player = "O" if self.current_player == "X" else "X"
        return None
    def check_winner(self):
        # Check rows, columns, and diagonals for a win
        for row in range(15):
            for col in range(15):
                if self.board[row][col] is not None:
                    if self.check_direction(row, col, 1, 0) or \
                       self.check_direction(row, col, 0, 1) or \
                       self.check_direction(row, col, 1, 1) or \
                       self.check_direction(row, col, 1, -1):
                        return self.board[row][col]  # Return the winning player's symbol
        return None  # No winner found
    def check_direction(self, row, col, delta_row, delta_col):
        '''
        Check for five in a row in a specific direction.
        '''
        count = 0
        for i in range(5):
            r = row + i * delta_row
            c = col + i * delta_col
            if 0 <= r < 15 and 0 <= c < 15 and self.board[r][c] == self.board[row][col]:
                count += 1
            else:
                break
        return count == 5
    def reset_game(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
    def __str__(self):
        board_str = ""
        for row in self.board:
            board_str += " ".join([cell if cell is not None else '.' for cell in row]) + "\n"
        return board_str