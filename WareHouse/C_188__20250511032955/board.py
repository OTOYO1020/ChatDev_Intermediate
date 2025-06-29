'''
Contains the Board class that manages the game logic for Gomoku.
'''
class Board:
    def __init__(self, game):
        self.game = game
        self.board = [["" for _ in range(15)] for _ in range(15)]
    def place_piece(self, x, y, player):
        if self.board[x][y] == "":
            self.board[x][y] = player
            return True
        else:
            print(f"Invalid move! Cell ({x}, {y}) is already occupied.")
            return False
    def check_winner(self, player):
        # Check horizontal, vertical, and diagonal for a win
        for i in range(15):
            for j in range(15):
                if self.board[i][j] == player:
                    if self.check_direction(i, j, 1, 0, player) or \
                       self.check_direction(i, j, 0, 1, player) or \
                       self.check_direction(i, j, 1, 1, player) or \
                       self.check_direction(i, j, 1, -1, player):
                        return True
        return False
    def check_direction(self, x, y, dx, dy, player):
        count = 0
        # Check in the positive direction
        for step in range(5):
            nx, ny = x + step * dx, y + step * dy
            if 0 <= nx < 15 and 0 <= ny < 15 and self.board[nx][ny] == player:
                count += 1
            else:
                break
        # Check in the negative direction
        for step in range(1, 5):
            nx, ny = x - step * dx, y - step * dy
            if 0 <= nx < 15 and 0 <= ny < 15 and self.board[nx][ny] == player:
                count += 1
            else:
                break
        return count >= 5
    def is_full(self):
        for row in self.board:
            if "" in row:
                return False
        return True
    def reset(self):
        self.board = [["" for _ in range(15)] for _ in range(15)]
    def display_board(self):
        for row in self.board:
            print(" ".join([cell if cell else "." for cell in row]))