'''
This file contains the Gomoku game logic and implementation without GUI.
'''
class GomokuGame:
    def __init__(self):
        self.board_size = 15
        self.board = [[0] * self.board_size for _ in range(self.board_size)]
        self.current_player = 1
        self.winner = None
    def make_move(self, x, y):
        if self.winner is not None:
            print("Game over! Player {} has already won.".format(self.winner))
            return  # Prevent further moves if the game is over
        if self.board[x][y] == 0:
            self.board[x][y] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
                print(f"Player {self.winner} wins!")  # Notify the win immediately
                return  # Prevent further moves
            self.current_player = 3 - self.current_player  # Switch between player 1 and 2
    def check_winner(self):
        # Check horizontal, vertical, and diagonal lines for a winner
        for x in range(self.board_size):
            for y in range(self.board_size):
                if self.board[x][y] != 0:
                    if self.check_line(x, y, 1, 0) or self.check_line(x, y, 0, 1) or \
                       self.check_line(x, y, 1, 1) or self.check_line(x, y, 1, -1):
                        return True
        return False
    def check_line(self, x, y, dx, dy):
        count = 0
        # Check in the positive direction
        for i in range(5):
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < self.board_size and 0 <= ny < self.board_size and self.board[nx][ny] == self.board[x][y]:
                count += 1
            else:
                break  # Stop if the sequence is broken
        # Check in the negative direction
        for i in range(1, 5):
            nx, ny = x - i * dx, y - i * dy
            if 0 <= nx < self.board_size and 0 <= ny < self.board_size and self.board[nx][ny] == self.board[x][y]:
                count += 1
            else:
                break  # Stop if the sequence is broken
        return count >= 5  # Return true if we have found 5 in a row
    def reset_game(self):
        self.board = [[0] * self.board_size for _ in range(self.board_size)]
        self.current_player = 1
        self.winner = None