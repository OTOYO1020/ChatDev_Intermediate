'''
Main entry point for the Gomoku game application.
'''
from board import Board
from player import Player
class GomokuGame:
    def __init__(self):
        self.board = Board(self)
        self.black_player = Player("Black")
        self.white_player = Player("White")
        self.current_player = self.black_player  # Start with Black player
    def play(self):
        while True:
            self.board.display_board()
            x, y = self.get_player_input()
            if self.board.place_piece(x, y, self.current_player.color):
                if self.board.check_win(self.current_player.color):
                    self.board.display_board()  # Display final board
                    print(f"{self.current_player.color} wins!")
                    break
                # Switch players
                self.current_player = self.white_player if self.current_player == self.black_player else self.black_player
    def get_player_input(self):
        while True:
            try:
                x, y = map(int, input(f"{self.current_player.color}'s turn. Enter row and column (0-14): ").split())
                if 0 <= x < 15 and 0 <= y < 15:
                    return x, y
                else:
                    print("Coordinates out of bounds. Please enter numbers between 0 and 14.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter two numbers between 0 and 14.")
if __name__ == "__main__":
    game = GomokuGame()
    game.play()