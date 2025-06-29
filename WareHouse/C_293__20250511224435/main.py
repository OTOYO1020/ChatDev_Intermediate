'''
Main application file for the Gomoku game.
'''
import sys
from board import Board
class GomokuGame:
    def __init__(self):
        self.board = Board()
        self.current_player = "X"
    def draw_board(self):
        for row in range(15):
            for col in range(15):
                piece = self.board.get_piece(row, col)
                print(f"{piece if piece else '.'}", end=' ')
            print()
    def make_move(self, row, col):
        if not (0 <= row < 15 and 0 <= col < 15):
            print("Invalid input: Please enter row and column between 0 and 14.")
            return
        if self.board.place_piece(row, col, self.current_player):
            self.draw_board()
            if self.check_winner(row, col):
                print(f"Player {self.current_player} wins!")
                self.reset_game()
                return  # Prevent further moves after a win
            elif self.board.is_full():
                print("The game is a draw! The board is full.")
                self.reset_game()
                return  # Prevent further moves after a draw
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
        else:
            print("Invalid Move: This cell is already occupied. Please choose another cell.")
    def check_winner(self, row, col):
        return self.board.check_winner(row, col, self.current_player)
    def reset_game(self):
        self.board.reset()
        self.current_player = "X"
        self.draw_board()
    def play(self):
        self.draw_board()
        while True:
            try:
                move = input(f"Player {self.current_player}, enter your move (row and column): ")
                row, col = map(int, move.split())
                self.make_move(row, col)
            except ValueError:
                print("Invalid input: Please enter two integers separated by a space.")
            except KeyboardInterrupt:
                print("\nGame exited.")
                sys.exit()
if __name__ == "__main__":
    game = GomokuGame()
    game.play()