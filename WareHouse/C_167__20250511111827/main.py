'''
Main entry point for the Gomoku game application.
'''
from board import Board
from player import Player
class GomokuGame:
    def __init__(self):
        self.board = Board()
        self.player1 = Player("Player 1", "X")
        self.player2 = Player("Player 2", "O")
        self.current_player = self.player1  # Start with Player 1
    def switch_player(self):
        """Switch the current player to the other player."""
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1
    def play_move(self, row, col):
        """
        Process the player's move on the board.
        Parameters:
        row (int): The row index for the move.
        col (int): The column index for the move.
        Returns:
        bool: True if the game ends (win or draw), False otherwise.
        """
        if 0 <= row < 15 and 0 <= col < 15:  # Validate input range
            if self.board.place_piece(row, col, self.current_player.symbol):
                if self.board.check_winner(self.current_player.symbol):
                    self.show_winner(self.current_player.name)
                    return True
                elif self.board.is_full():  # Check if the board is full
                    print("The game is a draw! The board is full.")
                    return True
                else:
                    self.switch_player()
            else:
                print("Invalid move. The cell is already occupied. Try again.")
        else:
            print("Invalid input. Please enter numbers between 0 and 14.")
        return False
    def show_winner(self, winner_name):
        """Display the winner of the game."""
        print(f"{winner_name} wins!")
    def start_game(self):
        """Start the game loop, allowing players to make moves."""
        while True:
            self.board.display_board()
            move = input(f"{self.current_player.name}, enter your move row (0-14) or type 'exit' to quit: ")
            if move.lower() == 'exit':
                print("Game exited.")
                break
            # Validate row input
            if not move.isdigit() or not (0 <= int(move) < 15):
                print("Invalid input. Please enter a number between 0 and 14.")
                continue
            row = int(move)
            # Validate column input
            col_input = input(f"{self.current_player.name}, enter your move column (0-14): ")
            if not col_input.isdigit() or not (0 <= int(col_input) < 15):
                print("Invalid input for column. Please enter a number between 0 and 14.")
                continue
            col = int(col_input)
            if self.play_move(row, col):
                break
if __name__ == "__main__":
    game = GomokuGame()
    game.start_game()