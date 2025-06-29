'''
This file contains the core logic for the Gomoku game, including the game state,
player moves, and win condition checks.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[0 for _ in range(15)] for _ in range(15)]
        self.current_player = 1
    def make_move(self, x, y):
        if x < 0 or x >= 15 or y < 0 or y >= 15:
            print("Invalid move. Coordinates are out of bounds.")
            return False, None  # Return False and no winner without switching players
        if self.board[x][y] != 0:
            print("Invalid move. The cell is already occupied.")
            return False, None  # Return False and no winner without switching players
        self.board[x][y] = self.current_player
        if self.check_winner(x, y):  # Pass the last move coordinates
            return True, self.current_player  # Return True and the winning player
        self.current_player = 3 - self.current_player  # Switch player
        return False, None  # Return False and no winner
    def check_winner(self, x, y):
        # Check if the last move made resulted in a win
        return self.check_line(x, y)
    def check_line(self, x, y):
        # Check all four possible winning directions
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 1
            # Check in the positive direction
            for step in range(1, 5):
                nx, ny = x + dx * step, y + dy * step
                if 0 <= nx < 15 and 0 <= ny < 15 and self.board[nx][ny] == self.board[x][y]:
                    count += 1
                else:
                    break
            # Check in the negative direction
            for step in range(1, 5):
                nx, ny = x - dx * step, y - dy * step
                if 0 <= nx < 15 and 0 <= ny < 15 and self.board[nx][ny] == self.board[x][y]:
                    count += 1
                else:
                    break
            # Ensure exactly 5 in a row for a win
            if count == 5:
                return True
        return False
    def reset_game(self):
        self.board = [[0 for _ in range(15)] for _ in range(15)]
        self.current_player = 1
        print("The game has been reset.")
    def print_board(self):
        for row in self.board:
            print(' '.join(['.' if cell == 0 else 'X' if cell == 1 else 'O' for cell in row]))