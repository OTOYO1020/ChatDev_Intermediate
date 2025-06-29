'''
This file contains the implementation of a basic Gomoku game using standard input and output.
'''
class GomokuGame:
    def __init__(self):
        self.board_size = 15
        self.board = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = "X"
        self.game_over = False  # New attribute to track game state
    def print_board(self):
        '''Prints the current state of the board.'''
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] is None:
                    print(".", end=" ")
                else:
                    print(self.board[row][col], end=" ")
            print()
        print()
    def make_move(self, row, col):
        '''Attempts to make a move on the board.'''
        if self.game_over:
            print("Game is over. No more moves can be made.")
            return False  # Indicate game is over
        if not (0 <= row < self.board_size and 0 <= col < self.board_size):
            print("Invalid move. Row and column must be within the board range.")
            return False
        if self.board[row][col] is None:
            self.board[row][col] = self.current_player
            if self.check_winner(row, col):
                print(f"Player {self.current_player} wins!")
                self.game_over = True  # Set game over
                return True
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")
        return False
    def check_winner(self, row, col):
        '''Checks if the current player has won the game.'''
        return (self.check_direction(row, col, 1, 0) or  # Horizontal
                self.check_direction(row, col, 0, 1) or  # Vertical
                self.check_direction(row, col, 1, 1) or  # Diagonal \
                self.check_direction(row, col, 1, -1))   # Diagonal /
    def check_direction(self, row, col, delta_row, delta_col):
        '''Checks for a winning condition in a specified direction.'''
        count = 0
        player = self.board[row][col]
        # Check in the positive direction
        r, c = row, col
        while 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == player:
            count += 1
            r += delta_row
            c += delta_col
        # Check in the negative direction
        r, c = row - delta_row, col - delta_col
        while 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == player:
            count += 1
            r -= delta_row
            c -= delta_col
        return count >= 5
    def reset_game(self):
        '''Resets the game to the initial state.'''
        self.board = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = "X"
        self.game_over = False  # Reset game state
def main():
    game = GomokuGame()
    while True:
        game.print_board()
        if game.game_over:
            print("Game is over. Thank you for playing!")
            reset = input("Would you like to play again? (y/n): ").strip().lower()
            if reset == 'y':
                game.reset_game()
            else:
                break  # Exit the loop if the game is over
            continue  # Skip to the next iteration to avoid prompting for moves
        try:
            row = int(input(f"Player {game.current_player}, enter your move row (0-{game.board_size-1}): "))
            col = int(input(f"Player {game.current_player}, enter your move column (0-{game.board_size-1}): "))
            if not game.make_move(row, col):
                print("Move was not successful. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers within the board range.")
if __name__ == "__main__":
    main()