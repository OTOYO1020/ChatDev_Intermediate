'''
Main file for the Gomoku game using standard input and output.
This file contains the main game loop and handles user input.
'''
class GomokuGame:
    def __init__(self):
        '''
        Initializes the Gomoku game with a 15x15 board and sets the current player to 1.
        '''
        self.board_size = 15
        self.board = [[0] * self.board_size for _ in range(self.board_size)]
        self.current_player = 1
        self.game_over = False  # Track if the game is over
    def print_board(self):
        '''
        Prints the current state of the board to the console.
        '''
        for row in self.board:
            print(' '.join(['.' if cell == 0 else 'X' if cell == 1 else 'O' for cell in row]))
    def make_move(self, row, col):
        '''
        Places a move on the board for the current player.
        Parameters:
        row (int): The row index for the move.
        col (int): The column index for the move.
        Returns:
        bool: True if the game is won after this move, False otherwise.
        '''
        if self.game_over:  # Check if the game is already won
            print("Game over! No more moves can be made.")
            return False
        if self.board[row][col] == 0:
            self.board[row][col] = self.current_player
            if self.check_winner():
                self.print_board()
                print(f"Player {self.current_player} wins!")
                self.game_over = True  # Set game over state
                return True
            self.current_player = 2 if self.current_player == 1 else 1
        else:
            print("Invalid move. Try again.")  # Keep the player in the loop
            return None  # Indicate that the move was invalid but do not change the turn
        return False
    def check_winner(self):
        '''
        Checks if the current player has won the game.
        Returns:
        bool: True if the current player has won, False otherwise.
        '''
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] != 0:
                    if (self.check_direction(row, col, 1, 0) or  # Horizontal
                        self.check_direction(row, col, 0, 1) or  # Vertical
                        self.check_direction(row, col, 1, 1) or  # Diagonal \
                        self.check_direction(row, col, 1, -1)):  # Diagonal /
                        return True
        return False
    def check_direction(self, row, col, delta_row, delta_col):
        '''
        Checks for a sequence of the current player's pieces in a specified direction.
        Parameters:
        row (int): The starting row index.
        col (int): The starting column index.
        delta_row (int): The change in row index for each step.
        delta_col (int): The change in column index for each step.
        Returns:
        bool: True if there are exactly 5 consecutive pieces, False otherwise.
        '''
        count = 0
        for i in range(5):  # Check for 5 in a row
            r = row + i * delta_row
            c = col + i * delta_col
            if 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == self.current_player:
                count += 1
            else:
                break
        # Check if the count is exactly 5 and ensure there are no additional pieces in both directions
        if count == 5:
            # Check the previous piece in the direction
            prev_r = row - delta_row
            prev_c = col - delta_col
            if 0 <= prev_r < self.board_size and 0 <= prev_c < self.board_size and self.board[prev_r][prev_c] == self.current_player:
                return False  # There is an additional piece before the sequence
            # Check the next piece in the direction
            next_r = row + 5 * delta_row
            next_c = col + 5 * delta_col
            if 0 <= next_r < self.board_size and 0 <= next_c < self.board_size and self.board[next_r][next_c] == self.current_player:
                return False  # There is an additional piece after the sequence
            return True  # Exactly 5 pieces in a row
        return False
    def reset_game(self):
        '''
        Resets the game board and current player to start a new game.
        '''
        self.board = [[0] * self.board_size for _ in range(self.board_size)]
        self.current_player = 1
        self.game_over = False  # Reset game over state
def main():
    '''
    Main function to run the Gomoku game.
    Handles user input and game loop.
    '''
    while True:
        game = GomokuGame()
        while True:
            game.print_board()
            try:
                row = int(input(f"Player {game.current_player}, enter your move row (0-{game.board_size-1}): "))
                col = int(input(f"Player {game.current_player}, enter your move column (0-{game.board_size-1}): "))
                if row < 0 or row >= game.board_size or col < 0 or col >= game.board_size:
                    print(f"Invalid input. Please enter numbers within the board range (0-{game.board_size-1}).")
                    continue
                result = game.make_move(row, col)  # Check if the move was successful
                if result is True:  # If the game is won, break the loop
                    break
                elif result is None:  # If the move was invalid, continue the loop
                    continue
            except ValueError:
                print("Invalid input. Please enter numbers within the board range.")
        # Reset the game for a new round
        game.reset_game()
        # Ask if players want to play again
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            break
if __name__ == "__main__":
    main()