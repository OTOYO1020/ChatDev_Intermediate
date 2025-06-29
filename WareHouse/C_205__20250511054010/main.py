'''
This is the main module that runs the Gomoku game application.
'''
from gomoku import GomokuGame
def main():
    game = GomokuGame()
    while True:
        game.print_board()
        try:
            row = int(input(f"Player {game.current_player}, enter your move row (0-14): "))
            col = int(input(f"Player {game.current_player}, enter your move column (0-14): "))
            if row < 0 or row > 14 or col < 0 or col > 14:
                print("Invalid move. Please enter row and column values between 0 and 14.")
                continue
            result = game.make_move(row, col)
            if result:
                game.print_board()
                print(result)
                break  # Exit the loop if there's a winner
        except (ValueError, IndexError):
            print("Invalid move. Please enter row and column values between 0 and 14.")
        if input("Do you want to continue playing? (y/n): ").lower() != 'y':
            break
if __name__ == "__main__":
    main()