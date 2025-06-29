'''
This is the entry point for the Gomoku game application.
'''
from gomoku import GomokuGame
def main():
    game = GomokuGame()
    while True:
        game.print_board()
        if game.winner:
            print(f"Player {game.winner} wins!")
            break
        if game.is_full():
            print("The game is a draw!")
            break
        while True:
            row_input = input(f"Player {game.current_player}, enter your move row (0-14): ")
            col_input = input(f"Player {game.current_player}, enter your move column (0-14): ")
            if row_input.isdigit() and col_input.isdigit():
                row = int(row_input)
                col = int(col_input)
                if 0 <= row < 15 and 0 <= col < 15:
                    game.make_move(row, col)
                    if game.winner or game.is_full():  # Check game state after the move
                        break  # Exit the input loop if the game is over
                    break  # Exit the input loop if the move is valid
                else:
                    print("Move out of bounds. Please enter values between 0 and 14.")
            else:
                print("Invalid input. Please enter integers only.")
if __name__ == "__main__":
    main()