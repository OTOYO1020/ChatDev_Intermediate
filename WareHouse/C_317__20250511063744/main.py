'''
Main entry point for the Gomoku game application.
'''
from gomoku_game import GomokuGame
def main():
    play_console()
def play_console():
    game = GomokuGame()
    while True:
        print(game)
        try:
            row = int(input(f"Player {game.current_player}, enter your move (row 0-14): "))
            col = int(input(f"Player {game.current_player}, enter your move (column 0-14): "))
            if not game.make_move(row, col):
                print("Invalid move, try again.")
            if game.winner:
                print(f"Player {game.winner} wins!")
                break
        except (ValueError, IndexError):
            print("Invalid input, please enter numbers between 0 and 14.")
if __name__ == "__main__":
    main()