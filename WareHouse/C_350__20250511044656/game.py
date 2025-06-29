'''
Contains the game logic for Gomoku.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
    def make_move(self, x, y):
        # Check if the move is within the bounds of the board
        if not (0 <= x < 15 and 0 <= y < 15):
            return "Invalid move! Coordinates must be between 0 and 14."
        if self.board[x][y] is not None:
            return "Invalid move! This cell is already occupied."
        self.board[x][y] = self.current_player
        if self.check_winner():
            return f"Player {self.current_player} wins!"
        self.current_player = "O" if self.current_player == "X" else "X"
        return None
    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
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
        count = 0
        for i in range(5):
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < 15 and 0 <= ny < 15 and self.board[nx][ny] == self.board[x][y]:
                count += 1
            else:
                break
        return count == 5
    def reset_game(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
    def display_board(self):
        for row in self.board:
            print(' '.join(['.' if cell is None else cell for cell in row]))