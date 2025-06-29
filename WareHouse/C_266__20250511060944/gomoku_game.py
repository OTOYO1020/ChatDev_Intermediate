'''
Contains the logic for the Gomoku game.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.winner = None
    def make_move(self, row, col):
        if not (0 <= row < 15 and 0 <= col < 15):
            print("Invalid move! Please enter row and column values between 0 and 14.")
            return False  # Indicate that the move was invalid
        if self.board[row][col] == ' ' and self.winner is None:
            self.board[row][col] = self.current_player
            if self.check_winner(row, col):
                self.winner = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True  # Indicate that the move was successful
        else:
            print("Invalid move! The cell is already occupied.")
            return False  # Indicate that the move was invalid
    def check_winner(self, row, col):
        return (self.check_line(row, col, 1, 0) or  # Horizontal
                self.check_line(row, col, 0, 1) or  # Vertical
                self.check_line(row, col, 1, 1) or  # Diagonal \
                self.check_line(row, col, 1, -1))   # Diagonal /
    def check_line(self, row, col, delta_row, delta_col):
        count = 0
        for direction in [1, -1]:
            r, c = row, col
            while 0 <= r < 15 and 0 <= c < 15 and self.board[r][c] == self.current_player:
                count += 1
                r += direction * delta_row
                c += direction * delta_col
        return count >= 5
    def reset_game(self):
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.winner = None
    def display_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 29)
    def is_board_full(self):
        return all(cell != ' ' for row in self.board for cell in row)