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
            print("Game over. Cannot make a move.")
            return
        if not (0 <= x < 15 and 0 <= y < 15):
            print("Invalid move. Coordinates are out of bounds.")
            return
        if self.board[x][y] is not None:
            print("Invalid move. The cell is already occupied.")
            return
        self.board[x][y] = self.current_player
        if self.check_winner():
            self.winner = self.current_player
        self.current_player = "O" if self.current_player == "X" else "X"
    def check_winner(self):
        # Check all cells for a potential winner
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
        # Check for a sequence of 5 or more pieces in the specified direction
        for i in range(5):  # Check for 5 pieces
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < 15 and 0 <= ny < 15 and self.board[nx][ny] == self.board[x][y]:
                count += 1
            else:
                break
        # Check in the opposite direction
        for i in range(1, 5):  # Check for additional pieces in the opposite direction
            nx, ny = x - i * dx, y - i * dy
            if 0 <= nx < 15 and 0 <= ny < 15 and self.board[nx][ny] == self.board[x][y]:
                count += 1
            else:
                break
        return count >= 5  # Ensure that there are at least 5 pieces in a row
    def is_board_full(self):
        return all(cell is not None for row in self.board for cell in row)
    def __str__(self):
        board_str = ""
        for row in self.board:
            board_str += " ".join([cell if cell is not None else '.' for cell in row]) + "\n"
        return board_str
    def reset_game(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.winner = None