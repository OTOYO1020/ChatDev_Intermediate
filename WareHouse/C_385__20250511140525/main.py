'''
Main file to run the Gomoku game using standard input and output.
'''
class GomokuGame:
    def __init__(self):
        self.board_size = 15
        self.board = self.create_board()
        self.current_player = 1  # Player 1 starts
        self.game_over = False  # Track if the game has ended
    def create_board(self):
        # Create an empty board
        return [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
    def print_board(self):
        # Print the current state of the board
        for row in self.board:
            print(' | '.join(row))
            print('-' * (self.board_size * 4 - 1))
    def on_click(self, x, y):
        if self.game_over:
            print("Game has already ended. Please reset to play again.")
            return False  # Prevent further moves
        if not (0 <= x < self.board_size and 0 <= y < self.board_size):
            print("Invalid move. Coordinates out of bounds.")
            return False  # Game continues without placing a piece
        if self.board[y][x] != ' ':
            print("Invalid move. Cell already occupied.")
            return False  # Game continues without placing a piece
        self.board[y][x] = 'X' if self.current_player == 1 else 'O'
        self.print_board()
        if self.check_winner(x, y):
            print(f"Player {self.current_player} Wins!")
            self.game_over = True  # Indicate that the game is over
            return True  # Indicate that the game is over
        if all(cell != ' ' for row in self.board for cell in row):
            print("The game is a draw!")
            self.game_over = True  # Indicate that the game is over
            return True  # Indicate that the game is over
        self.current_player = 3 - self.current_player  # Switch players
        return False  # Game continues
    def check_winner(self, x, y):
        # Check horizontal, vertical, and diagonal for a winner
        return (self.check_direction(x, y, 1, 0) or  # Horizontal
                self.check_direction(x, y, 0, 1) or  # Vertical
                self.check_direction(x, y, 1, 1) or  # Diagonal \
                self.check_direction(x, y, 1, -1))   # Diagonal /
    def check_direction(self, x, y, dx, dy):
        '''
        Check for five in a row in a specific direction.
        Parameters:
        x (int): The x-coordinate of the last move.
        y (int): The y-coordinate of the last move.
        dx (int): The change in x for the direction.
        dy (int): The change in y for the direction.
        '''
        count = 0
        for step in range(-4, 5):
            nx, ny = x + step * dx, y + step * dy
            if 0 <= nx < self.board_size and 0 <= ny < self.board_size:
                if self.board[ny][nx] == ('X' if self.current_player == 1 else 'O'):
                    count += 1
                    if count == 5:
                        return True
                else:
                    count = 0  # Reset count if the piece is from the opposite player or empty
            else:
                count = 0  # Reset count if out of bounds
        return False
    def reset_game(self):
        self.board = self.create_board()
        self.current_player = 1
        self.game_over = False  # Reset game over state
        print("Game has been reset.")
        self.print_board()
def main():
    '''
    Main function to run the game loop and handle user input.
    '''
    game = GomokuGame()  # Create a single instance of the game
    game.print_board()
    while True:
        move = input("Enter your move (x y) or 'r' to reset: ")
        if move.lower() == 'r':
            game.reset_game()
            continue
        # Validate input format
        if len(move.split()) != 2:
            print("Invalid input. Please enter two coordinates separated by a space.")
            continue
        try:
            x, y = map(int, move.split())
            if not (0 <= x < game.board_size and 0 <= y < game.board_size):
                print("Invalid move. Coordinates out of bounds.")
                continue
            if game.on_click(x, y):
                break  # Exit the loop if there's a winner or a draw
        except ValueError:
            print("Invalid input. Please enter valid coordinates.")
    if input("Do you want to play again? (y/n): ").lower() != 'y':
        return  # Exit the main loop if the user does not want to play again
if __name__ == "__main__":
    main()