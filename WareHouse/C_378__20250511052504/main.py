'''
Main entry point for the Gomoku game application.
'''
from gomoku_game import GomokuGame
def main():
    game = GomokuGame()
    while not game.game_over:
        print(game)
        try:
            row = int(input(f"Player {game.current_player}, enter your move row (0-14): "))
            col = int(input(f"Player {game.current_player}, enter your move column (0-14): "))
            game.make_move(row, col)
        except ValueError:
            print("Invalid input. Please enter integers only.")
            continue
        except IndexError:
            print("Invalid move. Please enter row and column between 0 and 14.")
            continue
        if game.game_over:
            print(game)
            print(f"Player {game.current_player} wins!")
if __name__ == "__main__":
    main()