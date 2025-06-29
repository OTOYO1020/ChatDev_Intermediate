'''
This module contains the command-line interface for the Gomoku game.
'''
from gomoku_game import GomokuGame  # Importing the GomokuGame class
def print_board(game):
    for row in game.board:
        print('|'.join(row))
        print('-' * (game.board_size * 2 - 1))
def cli_game():
    game = GomokuGame()
    while True:
        print_board(game)
        print(f"Current Player: {game.current_player}")
        try:
            x, y = map(int, input("Enter your move (row and column): ").split())
            if not (0 <= x < game.board_size and 0 <= y < game.board_size):
                print("Invalid move. Please enter numbers between 0 and 14.")
                continue  # Prompt for input again
            game.make_move(x, y)
            if game.winner:
                print_board(game)
                print(f"Player {game.winner} wins!")
                if input("Do you want to play again? (y/n): ").lower() != 'y':
                    break
                game.reset_game()
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")
        except Exception as e:
            print(e)
def main():
    while True:
        choice = input("Choose game mode: (1) Command Line (2) GUI (q to quit): ")
        if choice == '1':
            cli_game()
        elif choice == '2':
            print("GUI mode is not implemented in this version.")
        elif choice.lower() == 'q':
            break
        else:
            print("Invalid choice. Please select 1, 2, or q.")
if __name__ == "__main__":
    main()