'''
Main entry point for the Gomoku game application.
'''
from board import Board
class GomokuGame:
    def __init__(self):
        self.board = Board(self)
        self.reset_game()
    def reset_game(self):
        self.board.reset()
        print("New game started. Player X goes first.")
        self.print_board()
    def print_board(self):
        for row in self.board.grid:
            print(' '.join(['.' if cell == '' else cell for cell in row]))
    def place_piece(self, x, y):
        if self.board.place_piece(x, y):
            self.print_board()
            if self.board.check_winner():
                self.show_winner(self.board.winner)
            else:
                print(f"Player {self.board.current_player}'s turn.")
        else:
            print("Invalid move. Try again.")
    def show_winner(self, player):
        if player == 'Draw':
            print("The game is a draw!")
        else:
            print(f"Player {player} wins!")
        self.reset_game()
if __name__ == "__main__":
    game = GomokuGame()
    while True:
        try:
            x, y = map(int, input("Enter row and column (0-14) separated by space: ").split())
            if 0 <= x < 15 and 0 <= y < 15:
                game.place_piece(x, y)
            else:
                print("Coordinates out of bounds. Please enter values between 0 and 14.")
        except ValueError:
            print("Invalid input. Please enter two integers separated by space.")