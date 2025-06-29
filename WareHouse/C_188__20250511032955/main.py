'''
Main entry point for the Gomoku game application.
'''
from board import Board
class GomokuGame:
    def __init__(self):
        self.board = Board(self)
        self.current_player = "X"
        self.game_over = False
    def create_board(self):
        self.board.display_board()
    def make_move(self, x, y):
        if not self.game_over:
            if 0 <= x < 15 and 0 <= y < 15:  # Check for valid coordinates
                if self.board.place_piece(x, y, self.current_player):
                    self.board.display_board()
                    if self.board.check_winner(self.current_player):
                        print(f"Player {self.current_player} wins!")
                        self.game_over = True
                    elif self.board.is_full():
                        print("The game is a draw!")
                        self.game_over = True
                    else:
                        self.current_player = "O" if self.current_player == "X" else "X"
            else:
                print("Invalid move. Please enter numbers between 0 and 14.")
    def reset_game(self):
        self.board.reset()
        self.current_player = "X"
        self.game_over = False
        self.create_board()
if __name__ == "__main__":
    game = GomokuGame()
    game.create_board()
    while not game.game_over:
        try:
            x, y = map(int, input("Enter your move (row and column): ").split())
            game.make_move(x, y)
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")