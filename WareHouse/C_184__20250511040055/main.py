'''
This file contains the command-line implementation for the Gomoku game.
It manages the display and user interactions through standard input and output.
'''
from gomoku import GomokuGame
def main():
    game = GomokuGame()
    while True:
        game.print_board()
        print(f"Player {game.current_player}'s turn. Enter your move as 'row col': ")
        move = input()
        if move.lower() == 'exit':
            print("Exiting the game.")
            break
        try:
            x, y = map(int, move.split())
            game_over, winner = game.make_move(x, y)
            if game_over:
                game.print_board()
                print(f"Player {winner} wins!")
                break
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")
        except IndexError:
            print("Invalid move. Please try again.")
if __name__ == "__main__":
    main()