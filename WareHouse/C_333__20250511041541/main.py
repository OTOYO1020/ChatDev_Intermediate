'''
Main file to run the Gomoku game.
'''
from game import GomokuGame
def main():
    game = GomokuGame()
    while True:
        game.print_board()
        try:
            user_input = input(f"Current Player: {game.current_player}. Enter your move (row and column): ")
            coordinates = list(map(int, user_input.split()))
            if len(coordinates) != 2:
                print("Invalid input! Please enter exactly two integers separated by a space.")
                continue
            x, y = coordinates
            if not game.make_move(x, y):
                continue  # The error message is already printed in make_move
        except ValueError:
            print("Invalid input! Please enter two integers separated by a space.")
            continue
        except IndexError:
            print("Invalid input! Please enter row and column numbers between 0 and 14.")
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
    main()