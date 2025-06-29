'''
Contains the logic for the Gomoku game.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.winner = None
    def make_move(self, x, y):
        if self.winner is not None:
            print("Game is already over.")
            return False
        if self.is_board_full():
            print("Game is a draw. No more moves can be made.")
            return False
        if not (0 <= x < 15 and 0 <= y < 15):  # Check for valid coordinates
            print("Invalid move! Coordinates must be between 0 and 14.")
            return False
        if self.board[x][y] is not None:
            print("Invalid move! Cell is already occupied.")
            return False
        self.board[x][y] = self.current_player
        if self.check_winner():
            self.winner = self.current_player
        self.current_player = "O" if self.current_player == "X" else "X"
        return True
    def check_winner(self):
        # Check horizontal, vertical, and diagonal for a win
        for x in range(15):
            for y in range(15):
                if self.board[x][y] is not None:
                    if self.check_direction(x, y, 1, 0) or \
                       self.check_direction(x, y, 0, 1) or \
                       self.check_direction(x, y, 1, 1) or \
                       self.check_direction(x, y, 1, -1):
                        return True
        return False
    def check_direction(self, x, y, dx, dy):
        count = 1  # Start with the current piece
        # Check in the positive direction
        for i in range(1, 5):
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < 15 and 0 <= ny < 15 and self.board[nx][ny] == self.board[x][y]:
                count += 1
            else:
                break
        # Check in the negative direction
        for i in range(1, 5):
            nx, ny = x - i * dx, y - i * dy
            if 0 <= nx < 15 and 0 <= ny < 15 and self.board[nx][ny] == self.board[x][y]:
                count += 1
            else:
                break
        # Check if we counted five in a row
        return count >= 5
    def is_board_full(self):
        return all(cell is not None for row in self.board for cell in row)
    def print_board(self):
        for row in self.board:
            print(' '.join(['.' if cell is None else cell for cell in row]))