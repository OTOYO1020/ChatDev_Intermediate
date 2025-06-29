'''
This is the main entry point for the Gomoku game application.
'''
from gomoku_game import GomokuGame
def main():
    game = GomokuGame()
    while True:
        game.print_board()
        if game.winner:
            print(f"Player {game.winner} wins!")
            break
        try:
            row = int(input(f"Current Player: {game.current_player}. Enter row (0-14): "))
            col = int(input(f"Enter column (0-14): "))
            if not (0 <= row < 15 and 0 <= col < 15):
                print("Invalid input. Please enter numbers between 0 and 14.")
                continue
            game.make_move(row, col)
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 14.")
        except IndexError:
            print("Invalid move. Please try again.")
if __name__ == "__main__":
    main()