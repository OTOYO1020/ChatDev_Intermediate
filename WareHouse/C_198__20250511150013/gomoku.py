'''
Contains the game logic for the Gomoku game.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[0 for _ in range(15)] for _ in range(15)]
        self.current_player = 1
        self.winner = None
    def make_move(self, x, y):
        if self.winner is not None:
            print("Game has already ended. No further moves can be made.")
            return False
        if 0 <= x < 15 and 0 <= y < 15 and self.board[x][y] == 0:
            self.board[x][y] = self.current_player
            if self.check_win():
                self.winner = self.current_player
            self.current_player = 3 - self.current_player  # Switch between player 1 and 2
            return True
        return False
    def check_win(self):
        # Check horizontal, vertical, and diagonal for a win
        for x in range(15):
            for y in range(15):
                if self.board[x][y] != 0:
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
        return count >= 5  # Return true if there are 5 or more in a row
    def print_board(self):
        for row in self.board:
            print(' '.join(['.' if cell == 0 else 'X' if cell == 1 else 'O' for cell in row]))