'''
Main entry point for the Gomoku game application.
'''
from gomoku_game import GomokuGame
def run():
    game = GomokuGame()
    while True:
        game.print_board()
        try:
            x, y = map(int, input(f"Current Player: {game.current_player}. Enter your move (row and column): ").split())
            if not game.make_move(x, y):
                print("Invalid move. Please choose another cell.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid row and column numbers between 0 and 14.")
            continue
        if game.winner:
            game.print_board()
            print(f"Player {game.winner} wins!")
            break
        if game.is_board_full():
            game.print_board()
            print("The game is a draw!")
            break
if __name__ == "__main__":
    run()