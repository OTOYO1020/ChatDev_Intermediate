'''
Main entry point for the Gomoku game application.
'''
from gomoku_logic import GomokuLogic
class GomokuGame:
    def __init__(self):
        self.logic = GomokuLogic()
        self.board_size = 15
        self.reset_game()
    def draw_board(self):
        """Draws the current state of the board."""
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.logic.board[row][col] == 1:
                    print("B", end=" ")  # Black piece
                elif self.logic.board[row][col] == 2:
                    print("W", end=" ")  # White piece
                else:
                    print(".", end=" ")  # Empty cell
            print()  # New line after each row
    def handle_click(self, row, col):
        """Handles a player's move and checks for a winner or draw."""
        if self.logic.make_move(row, col):
            self.draw_board()
            if self.logic.is_winner():
                print(f"Player {self.logic.current_player} wins!")
                self.reset_game()
            elif self.logic.is_draw():
                print("It's a draw!")
                self.reset_game()
        else:
            print("Invalid move. Cell is already occupied.")
    def reset_game(self):
        """Resets the game to the initial state."""
        self.logic.reset_game()
        self.draw_board()
if __name__ == "__main__":
    game = GomokuGame()
    while True:
        try:
            user_input = input("Enter row (0-14) or 'exit' to quit: ")
            if user_input.lower() == 'exit':
                print("Thanks for playing!")
                break
            row = int(user_input)
            col = int(input("Enter column (0-14): "))
            if 0 <= row < 15 and 0 <= col < 15:
                game.handle_click(row, col)
            else:
                print("Invalid input. Please enter values between 0 and 14.")
        except ValueError:
            print("Invalid input. Please enter integers.")