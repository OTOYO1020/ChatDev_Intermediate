'''
Main entry point for the Gomoku game application.
'''
from gomoku_game import GomokuGame
def main():
    game = GomokuGame()
    while True:
        game.print_board()
        try:
            row = int(input(f"Player {game.current_player}, enter your move row (0-14): "))
            col = int(input(f"Player {game.current_player}, enter your move column (0-14): "))
            move_result = game.make_move(row, col)
            if move_result is not True:
                print(move_result)  # Print the specific error message
                continue
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 14.")
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