'''
Main file to run the Gomoku game.
'''
from board import Board
class GomokuGame:
    def __init__(self):
        self.board = Board()
        self.current_player = "X"
        self.play_game()
    def play_game(self):
        while True:
            self.board.display()
            print(f"Player {self.current_player}'s turn.")
            try:
                x, y = map(int, input("Enter your move (row and column): ").split())
                if self.board.make_move(x, y, self.current_player):
                    if self.board.check_winner():
                        self.board.display()
                        print(f"Player {self.current_player} wins!")
                        if input("Do you want to play again? (y/n): ").lower() == 'y':
                            self.board = Board()  # Reset the game
                        else:
                            break
                    elif self.board.is_draw():
                        self.board.display()
                        print("The game is a draw!")
                        if input("Do you want to play again? (y/n): ").lower() == 'y':
                            self.board = Board()  # Reset the game
                        else:
                            break
                    self.current_player = "O" if self.current_player == "X" else "X"
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")
            except IndexError:
                print("Invalid move. Please enter numbers between 0 and 14.")
if __name__ == "__main__":
    game = GomokuGame()