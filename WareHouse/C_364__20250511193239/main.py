'''
Main file to run the Gomoku game.
'''
from board import Board
class GomokuGame:
    def __init__(self):
        self.board = Board()
    def run(self):
        while True:
            self.board.display_board()
            user_input = input(f"{self.board.current_player}'s turn. Enter row and column (0-14) or 'exit' to quit: ")
            if user_input.lower() == 'exit':
                print("Thanks for playing!")
                break
            try:
                x, y = map(int, user_input.split())
                if not self.board.place_piece(x, y):
                    print("Invalid move. Try again.")
                elif self.board.is_full():
                    print("The board is full! It's a draw!")
                    break
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space or 'exit' to quit.")
if __name__ == "__main__":
    game = GomokuGame()
    game.run()