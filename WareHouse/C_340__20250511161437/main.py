'''
Main entry point for the Gomoku game application.
'''
from gomoku_game import GomokuGame
def main():
    game = GomokuGame()
    while True:
        game.display_board()
        try:
            row = int(input(f"Player {game.current_player}, enter your move row (0-14): "))
            col = int(input(f"Player {game.current_player}, enter your move column (0-14): "))
            game.make_move(row, col)
        except ValueError as e:
            print(e)  # Print the error message from the exception
            continue
        if game.is_game_over():
            game.display_board()
            if game.winner:
                print(f"Player {game.winner} wins!")
            else:
                print("The game is a draw!")
            break
if __name__ == "__main__":
    main()