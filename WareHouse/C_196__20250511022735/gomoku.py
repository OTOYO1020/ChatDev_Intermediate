'''
Contains the logic for the Gomoku game, including game state management.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
    def make_move(self, x, y):
        if x < 0 or x >= 15 or y < 0 or y >= 15:
            return "Invalid move. Coordinates out of bounds."
        if self.board[x][y] is None:
            self.board[x][y] = self.current_player
            winner = self.check_winner()
            if winner:
                return f"Player {winner} wins!"
            self.current_player = "O" if self.current_player == "X" else "X"
            return None
        else:
            return "Invalid move. Cell is already occupied."
    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for x in range(15):
            for y in range(15):
                if self.board[x][y] is not None:
                    if self.check_direction(x, y, 1, 0) or \
                       self.check_direction(x, y, 0, 1) or \
                       self.check_direction(x, y, 1, 1) or \
                       self.check_direction(x, y, 1, -1):
                        return self.board[x][y]  # Return the winning player
        return None  # No winner
    def check_direction(self, x, y, dx, dy):
        count = 0
        for i in range(5):
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < 15 and 0 <= ny < 15 and self.board[nx][ny] == self.board[x][y]:
                count += 1
            else:
                break
        return count == 5  # Check for exactly 5 in a row
    def reset_game(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
    def display_board(self):
        for row in self.board:
            print(' '.join(['.' if cell is None else cell for cell in row]))