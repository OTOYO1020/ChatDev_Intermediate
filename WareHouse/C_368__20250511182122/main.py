'''
Gomoku Game Implementation using standard input and output
This file contains the main class GomokuGame that initializes the game,
manages the game logic, and allows players to interact through the console.
'''
class GomokuGame:
    def __init__(self):
        """Initializes the Gomoku game with a 15x15 board and sets the current player to 1."""
        self.board_size = 15
        self.board = [[0] * self.board_size for _ in range(self.board_size)]
        self.current_player = 1
    def print_board(self):
        """Prints the current state of the board."""
        for row in self.board:
            print(' '.join(['.' if cell == 0 else 'X' if cell == 1 else 'O' for cell in row]))
    def on_click(self, x, y):
        """Handles a player's move by placing a piece on the board if the move is valid.
        Args:
            x (int): The column index for the move.
            y (int): The row index for the move.
        Returns:
            bool: True if the game is won by the current player, False otherwise.
        """
        # Validate input coordinates
        if x < 0 or x >= self.board_size or y < 0 or y >= self.board_size:
            print("Invalid move. Coordinates are out of bounds. Try again.")
            return False
        if self.board[y][x] == 0:
            self.board[y][x] = self.current_player
            self.print_board()
            if self.check_winner(x, y):
                print(f"Player {self.current_player} wins!")
                return True
            self.current_player = 3 - self.current_player  # Switch between player 1 and 2
        else:
            print("Invalid move. Cell already occupied. Try again.")
        return False
    def check_winner(self, x, y):
        """Checks if the current player has won the game after their move.
        Args:
            x (int): The column index of the last move.
            y (int): The row index of the last move.
        Returns:
            bool: True if the current player has won, False otherwise.
        """
        return (self.check_direction(x, y, 1, 0) or  # Horizontal
                self.check_direction(x, y, 0, 1) or  # Vertical
                self.check_direction(x, y, 1, 1) or  # Diagonal \
                self.check_direction(x, y, 1, -1))   # Diagonal /
    def check_direction(self, x, y, dx, dy):
        """Checks for five consecutive pieces in a given direction.
        Args:
            x (int): The starting column index.
            y (int): The starting row index.
            dx (int): The change in column index for each step.
            dy (int): The change in row index for each step.
        Returns:
            bool: True if five consecutive pieces are found, False otherwise.
        """
        count = 0
        for step in range(-4, 5):
            nx, ny = x + step * dx, y + step * dy
            if 0 <= nx < self.board_size and 0 <= ny < self.board_size:
                if self.board[ny][nx] == self.current_player:
                    count += 1
                    if count == 5:
                        return True  # Return immediately upon finding 5 consecutive pieces
                else:
                    count = 0  # Reset count if a non-matching piece is found
            else:
                count = 0  # Reset count if out of bounds
        return False
    def is_board_full(self):
        """Checks if the board is full.
        Returns:
            bool: True if the board is full, False otherwise.
        """
        return all(cell != 0 for row in self.board for cell in row)
    def reset_game(self):
        """Resets the game board and current player to start a new game."""
        self.board = [[0] * self.board_size for _ in range(self.board_size)]
        self.current_player = 1
        print("Game has been reset.")
        self.print_board()
if __name__ == "__main__":
    game = GomokuGame()
    game.print_board()
    while True:
        try:
            x, y = map(int, input(f"Player {game.current_player}, enter your move (row and column) or type 'reset' to reset the game: ").split())
            if game.on_click(x, y):
                break
            if game.is_board_full():
                print("The game is a draw! The board is full.")
                break
        except ValueError:
            if input("Type 'reset' to reset the game or 'exit' to quit: ").strip().lower() == 'reset':
                game.reset_game()
            elif input("Type 'exit' to quit the game: ").strip().lower() == 'exit':
                print("Exiting the game.")
                break
            else:
                print("Invalid input. Please enter row and column as two numbers separated by space.")