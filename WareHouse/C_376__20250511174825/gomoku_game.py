'''
This module contains the logic for the Gomoku game.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.winner = None
    def make_move(self, x, y):
        if not (0 <= x < 15 and 0 <= y < 15):
            print("Move out of bounds. Please enter values between 0 and 14.")
            return False
        if self.board[x][y] is None and self.winner is None:
            self.board[x][y] = self.current_player
            if self.check_win():
                self.winner = self.current_player
            elif self.is_draw():
                self.winner = "Draw"
            self.current_player = "O" if self.current_player == "X" else "X"
            return True
        else:
            print("Invalid move. Cell is already occupied.")
            return False
    def check_win(self):
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
        self.winner = None
    def is_draw(self):
        return all(cell is not None for row in self.board for cell in row)
    def __str__(self):
        board_str = ""
        for row in self.board:
            board_str += " ".join(['.' if cell is None else cell for cell in row]) + "\n"
        return board_str