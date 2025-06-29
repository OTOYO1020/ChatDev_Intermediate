'''
Main entry point for the Gomoku game application.
'''
from gomoku import GomokuGame
def main():
    game = GomokuGame()
    run_console_game(game)
def run_console_game(game):
    while True:
        game.print_board()
        try:
            x, y = map(int, input(f"Player {game.current_player}, enter your move (row and column): ").split())
            # Check if the input is within bounds before making a move
            if x < 0 or x >= 15 or y < 0 or y >= 15:
                print("Invalid input. Please enter two numbers between 0 and 14.")
                continue
            if not game.make_move(x, y):
                print("Invalid move. The cell is already occupied. Try again.")
        except ValueError:
            print("Invalid input. Please enter two numbers between 0 and 14.")
            continue
        if game.winner:
            game.print_board()
            print(f"Player {game.winner} wins!")
            break
if __name__ == "__main__":
    main()