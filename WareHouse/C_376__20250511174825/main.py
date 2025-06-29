'''
This module contains the command-line interface and entry point for the Gomoku game.
'''
from gomoku_game import GomokuGame
def print_board(game):
    print(game)
def main():
    game = GomokuGame()
    play_cli(game)
def play_cli(game):
    while game.winner is None:
        print_board(game)
        try:
            x, y = map(int, input(f"Player {game.current_player}, enter your move (row and column): ").split())
            if not game.make_move(x, y):
                print("Try again.")
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")
    print_board(game)
    if game.winner == "Draw":
        print("The game is a draw!")
    else:
        print(f"Player {game.winner} wins!")
if __name__ == "__main__":
    main()