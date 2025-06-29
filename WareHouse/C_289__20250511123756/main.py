'''
This file contains the implementation of a basic Gomoku game using standard input and output.
'''
class GomokuGame:
    def __init__(self):
        self.board_size = 15
        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 1
        self.game_over = False  # Track if the game is over
    def draw_board(self):
        """Draws the current state of the board."""
        print("  " + " ".join(str(i) for i in range(self.board_size)))
        for i in range(self.board_size):
            row = str(i) + " "
            for j in range(self.board_size):
                if self.board[i][j] == 0:
                    row += ". "
                elif self.board[i][j] == 1:
                    row += "X "
                else:
                    row += "O "
            print(row)
    def on_click(self, row, col):
        """Handles a player's move on the board."""
        if self.game_over:
            print("Game is over. Please reset to play again.")
            return
        if self.board[row][col] == 0:
            self.board[row][col] = self.current_player
            if self.check_winner(row, col):
                print(f"Player {self.current_player} wins!")
                self.game_over = True  # Set game_over to True
            else:
                self.current_player = 2 if self.current_player == 1 else 1
            self.draw_board()
        else:
            print("Invalid move, that space is already occupied. Try again.")
    def check_winner(self, row, col):
        """Checks if the current player has won the game."""
        # Check horizontal, vertical, and both diagonal directions for a win
        for dr, dc in [(0, 1), (1, 0), (1, 1), (1, -1)]:
            count = 1
            for d in [1, -1]:
                r, c = row, col
                while 0 <= r + d * dr < self.board_size and 0 <= c + d * dc < self.board_size and self.board[r + d * dr][c + d * dc] == self.current_player:
                    count += 1
                    r += d * dr
                    c += d * dc
            if count >= 5:
                return True
        return False
    def reset_game(self):
        """Resets the game to the initial state."""
        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 1
        self.game_over = False  # Reset game_over to False
        print("Game reset.")
        self.draw_board()
    def play(self):
        """Starts the game and handles player input."""
        print("Welcome to Gomoku!")
        self.draw_board()
        while True:
            try:
                move = input(f"Player {self.current_player}, enter your move (row,col 0-{self.board_size-1}): ")
                row, col = map(int, move.split(','))
                if 0 <= row < self.board_size and 0 <= col < self.board_size:
                    self.on_click(row, col)
                else:
                    print("Move out of bounds, please enter a valid move.")
            except ValueError:
                print("Invalid input, please enter in the format 'row,col' with numbers.")
if __name__ == "__main__":
    game = GomokuGame()
    game.play()