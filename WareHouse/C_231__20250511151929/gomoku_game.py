'''
This module contains the logic for the Gomoku game.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.winner = None
    def make_move(self, x, y):
        if 0 <= x < 15 and 0 <= y < 15 and self.board[x][y] == ' ' and self.winner is None:
            self.board[x][y] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        elif self.winner is not None:
            print("Game over! No further moves can be made.")
    def check_winner(self):
        # Check horizontal, vertical, and diagonal for a win
        for x in range(15):
            for y in range(15):
                if self.board[x][y] != ' ':
                    if self.check_direction(x, y, 1, 0) or \
                       self.check_direction(x, y, 0, 1) or \
                       self.check_direction(x, y, 1, 1) or \
                       self.check_direction(x, y, 1, -1):
                        return True
        return False
    def check_direction(self, x, y, dx, dy):
        count = 0
        for i in range(-4, 5):  # Check in both directions (negative and positive)
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < 15 and 0 <= ny < 15 and self.board[nx][ny] == self.board[x][y]:
                count += 1
                if count >= 5:  # Check if we have 5 in a row
                    return True
            else:
                if count > 0:  # Only reset if we had counted some pieces
                    break  # Exit the loop if the sequence is broken
        return False
    def reset_game(self):
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.winner = None
    def __str__(self):
        board_str = '\n'.join(['|'.join(row) for row in self.board])
        return board_str