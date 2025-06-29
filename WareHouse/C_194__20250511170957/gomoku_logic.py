'''
Contains the game logic for the Gomoku game.
'''
class GomokuLogic:
    def __init__(self):
        self.board = [[0] * 15 for _ in range(15)]
        self.current_player = 1
        self.move_count = 0
    def make_move(self, row, col):
        """Places a piece on the board for the current player."""
        if self.board[row][col] == 0:
            self.board[row][col] = self.current_player
            self.move_count += 1
            self.current_player = 2 if self.current_player == 1 else 1
            return True
        return False
    def is_winner(self):
        """Checks if the current player has won the game."""
        for row in range(15):
            for col in range(15):
                if self.board[row][col] != 0 and self.check_winner(row, col):
                    return True
        return False
    def check_winner(self, row, col):
        """Checks for a winning condition from the given position."""
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            # Check in the positive direction
            for step in range(1, 5):
                r, c = row + dr * step, col + dc * step
                if 0 <= r < 15 and 0 <= c < 15 and self.board[r][c] == self.board[row][col]:
                    count += 1
                else:
                    break
            # Check in the negative direction
            for step in range(1, 5):
                r, c = row - dr * step, col - dc * step
                if 0 <= r < 15 and 0 <= c < 15 and self.board[r][c] == self.board[row][col]:
                    count += 1
                else:
                    break
            if count >= 5:
                return True
        return False
    def is_draw(self):
        """Checks if the game is a draw."""
        return all(cell != 0 for row in self.board for cell in row)
    def reset_game(self):
        """Resets the game board and player settings."""
        self.board = [[0] * 15 for _ in range(15)]
        self.current_player = 1
        self.move_count = 0