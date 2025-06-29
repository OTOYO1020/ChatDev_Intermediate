'''
Contains the GomokuGame class that manages the game logic.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.game_over = False  # Track if the game is over
    def make_move(self, row, col):
        # Check if the game is already over
        if self.game_over:
            return "Game over. Player {} has already won!".format("O" if self.current_player == "X" else "X")
        # Validate the move
        if row < 0 or row >= 15 or col < 0 or col >= 15:
            return "Invalid move. Row and column must be between 0 and 14."
        # Check if the cell is empty
        if self.board[row][col] is None:
            self.board[row][col] = self.current_player
            if self.check_winner(row, col):
                self.game_over = True  # Set game over flag
                return f"Player {self.current_player} wins!"
            self.current_player = "O" if self.current_player == "X" else "X"
            return None
        else:
            return "Invalid move. Cell is already occupied."
    def check_winner(self, row, col):
        # Check horizontal, vertical, and diagonal for a win
        return (self.check_direction(row, col, 1, 0) or  # Horizontal
                self.check_direction(row, col, 0, 1) or  # Vertical
                self.check_direction(row, col, 1, 1) or  # Diagonal \
                self.check_direction(row, col, 1, -1))   # Diagonal /
    def check_direction(self, row, col, delta_row, delta_col):
        # Count the number of consecutive pieces in both directions
        count = 1
        for direction in (1, -1):
            r, c = row, col
            while True:
                r += direction * delta_row
                c += direction * delta_col
                if 0 <= r < 15 and 0 <= c < 15 and self.board[r][c] == self.board[row][col]:
                    count += 1
                else:
                    break
        return count >= 5
    def reset_game(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.game_over = False  # Reset game over flag
    def display_board(self):
        for row in self.board:
            print(" ".join(['.' if cell is None else cell for cell in row]))