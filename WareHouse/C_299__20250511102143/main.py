'''
This module contains the main application for the Gomoku game.
'''
from gomoku_game import GomokuGame  # Importing GomokuGame class
def main():
    game = GomokuGame()
    while True:
        game.print_board()
        print(f"Player {game.current_player}'s turn.")
        try:
            row = int(input("Enter row (0-14): "))
            col = int(input("Enter column (0-14): "))
            result = game.make_move(row, col)
            if result == "Invalid move. Cell already occupied.":
                print(result)
                continue
            if game.winner:
                game.print_board()
                if game.winner == "Draw":
                    print("It's a draw!")
                else:
                    print(f"Player {game.winner} wins!")
                break
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 14.")
if __name__ == "__main__":
    main()