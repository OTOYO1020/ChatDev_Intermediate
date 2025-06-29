'''
Main entry point for the Gomoku game application.
'''
from board import Board
import sys
class GomokuGame:
    def __init__(self):
        self.board = Board(self)
        self.board.draw_board()
    def reset_game(self):
        self.board.reset_game()
if __name__ == "__main__":
    game = GomokuGame()
    game.board.draw_board()  # Draw the initial board
    while True:
        try:
            command = input("Enter your move as 'x y' (or 'reset' to reset the game, 'exit' to quit): ").strip().lower()
            if command == 'reset':
                game.reset_game()
            elif command == 'exit':
                print("Exiting the game.")
                sys.exit()
            else:
                try:
                    x, y = map(int, command.split())
                    game.board.make_move(x, y)
                except ValueError:
                    print("Invalid input! Please enter your move as 'x y'.")
        except KeyboardInterrupt:
            print("\nExiting the game.")
            sys.exit()