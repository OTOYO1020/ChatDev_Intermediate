'''
Main entry point for the Gomoku game application.
'''
import sys
from gomoku_logic import GomokuLogic
class GomokuGame:
    def __init__(self):
        self.board_size = 15
        self.logic = GomokuLogic(self.board_size)
        self.current_player = 1  # Player 1 starts
        self.play_game()
    def play_game(self):
        while True:
            self.print_board()
            x, y = self.get_move()
            if self.logic.place_stone(x, y, self.current_player):
                if self.logic.is_winner(self.current_player):
                    self.print_board()
                    print(f"Player {self.current_player} wins!")
                    if self.play_again():
                        self.logic.reset()
                        self.current_player = 1  # Reset to Player 1
                    else:
                        print("Thanks for playing!")
                        break
                elif self.logic.is_board_full():
                    self.print_board()
                    print("It's a draw!")
                    if self.play_again():
                        self.logic.reset()
                        self.current_player = 1  # Reset to Player 1
                    else:
                        print("Thanks for playing!")
                        break
                self.current_player = 3 - self.current_player  # Switch player
            else:
                print("Invalid move, try again.")
    def print_board(self):
        for row in self.logic.board:
            print(' '.join(['.' if cell == 0 else 'X' if cell == 1 else 'O' for cell in row]))
    def get_move(self):
        while True:
            try:
                move = input(f"Player {self.current_player}, enter your move (row and column): ")
                x, y = map(int, move.split())
                if 0 <= x < self.board_size and 0 <= y < self.board_size:
                    return x, y
                else:
                    print("Move out of bounds, try again.")
            except ValueError:
                print("Invalid input, please enter two numbers separated by a space.")
    def play_again(self):
        while True:
            response = input("Do you want to play again? (y/n): ").strip().lower()
            if response in ['y', 'yes']:
                return True
            elif response in ['n', 'no']:
                return False
            else:
                print("Invalid input, please enter 'y' or 'n'.")
if __name__ == "__main__":
    GomokuGame()