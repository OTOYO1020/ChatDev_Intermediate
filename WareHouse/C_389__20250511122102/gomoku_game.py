'''
Class to handle the logic of the Gomoku game.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.winner = None
    def make_move(self, row, col):
        if self.winner is not None:
            return False  # Prevent any moves if there is already a winner
        if 0 <= row < 15 and 0 <= col < 15 and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            if self.check_winner(row, col):
                self.winner = self.current_player
                return True
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        print("This position is already taken or out of bounds.")  # Specific feedback for invalid moves
        return False
    def check_winner(self, row, col):
        # Check horizontal, vertical, and diagonal lines for a win
        return (self.check_line(row, col, 1, 0) or  # Horizontal
                self.check_line(row, col, 0, 1) or  # Vertical
                self.check_line(row, col, 1, 1) or  # Diagonal \
                self.check_line(row, col, 1, -1))   # Diagonal /
    def check_line(self, row, col, delta_row, delta_col):
        count = 1  # Start with the current move
        # Check in both directions
        for direction in [1, -1]:
            for step in range(1, 5):  # Check the next 4 spaces
                r = row + step * delta_row * direction
                c = col + step * delta_col * direction
                if 0 <= r < 15 and 0 <= c < 15 and self.board[r][c] == self.current_player:
                    count += 1
                else:
                    break
                if count == 5:  # Stop counting if we have exactly 5
                    return True
        return False  # Return false if less than 5 in a row
    def reset_game(self):
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.winner = None
    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 29)