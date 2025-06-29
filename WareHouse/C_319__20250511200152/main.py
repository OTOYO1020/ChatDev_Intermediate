'''
This module serves as the entry point for the Gomoku game application.
'''
from gomoku_game import GomokuGame
def main():
    game = GomokuGame()
    while True:
        game.print_board()
        try:
            x = int(input(f"Player {game.current_player}, enter your move (row): ").strip())
            y = int(input(f"Player {game.current_player}, enter your move (column): ").strip())
            if x < 0 or x > 14 or y < 0 or y > 14:
                print("Invalid move. Please enter row and column values between 0 and 14.")
                continue
            result = game.make_move(x, y)
            if result:
                print(result)
                game.print_board()
                if "wins" in result or "draw" in result:
                    break
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except IndexError:
            print("Invalid move. Please enter row and column values between 0 and 14.")
if __name__ == "__main__":
    main()