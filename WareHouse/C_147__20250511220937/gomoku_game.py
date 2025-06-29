'''
Contains the logic for the Gomoku game.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.game_over = False
    def make_move(self, x, y):
        if self.game_over:
            return "Game over! Please restart to play again."
        # Check if the coordinates are within the bounds of the board
        if x < 0 or x >= 15 or y < 0 or y >= 15:
            return "Invalid move! Coordinates are out of bounds."
        if self.board[x][y] is None:
            self.board[x][y] = self.current_player
            if self.check_winner():
                self.game_over = True
                return f"Player {self.current_player} wins!"
            self.current_player = "O" if self.current_player == "X" else "X"
        else:
            return "Invalid move! Cell is already occupied."
        return None
    def check_winner(self):
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
        player_piece = self.board[x][y]
        for i in range(5):  # Check for 5 in a row
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < 15 and 0 <= ny < 15 and self.board[nx][ny] == player_piece:
                count += 1
            else:
                break
        # Ensure that we return True if five or more pieces are found in a row
        return count >= 5  # This line checks for five or more pieces.
    def reset_game(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.game_over = False
    def display_board(self):
        for row in self.board:
            print(' '.join(['.' if cell is None else cell for cell in row]))