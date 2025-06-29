'''
Contains the logic for the Gomoku game, including game state management and win condition checks.
'''
class GomokuLogic:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [[0] * board_size for _ in range(board_size)]
    def place_stone(self, x, y, player):
        if self.board[x][y] == 0:  # Check if the cell is empty
            self.board[x][y] = player
            return True
        return False
    def is_winner(self, player):
        # Check horizontal, vertical, and diagonal for a win
        for x in range(self.board_size):
            for y in range(self.board_size):
                if self.board[x][y] == player and self.check_direction(x, y, player):
                    return True
        return False
    def check_direction(self, x, y, player):
        if self.board[x][y] != player:
            return False
        # Check all directions
        return (self.check_line(x, y, 1, 0, player) or  # Horizontal
                self.check_line(x, y, 0, 1, player) or  # Vertical
                self.check_line(x, y, 1, 1, player) or  # Diagonal \
                self.check_line(x, y, 1, -1, player))   # Diagonal /
    def check_line(self, x, y, dx, dy, player):
        count = 0
        for i in range(5):  # Check for exactly 5 in a row
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < self.board_size and 0 <= ny < self.board_size and self.board[nx][ny] == player:
                count += 1
            else:
                break
        # Ensure that we only return True if exactly 5 stones are found
        return count == 5
    def reset(self):
        self.board = [[0] * self.board_size for _ in range(self.board_size)]
    def is_board_full(self):
        return all(cell != 0 for row in self.board for cell in row)