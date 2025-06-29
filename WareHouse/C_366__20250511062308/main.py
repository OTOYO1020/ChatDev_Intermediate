'''
This is the main entry point for the Gomoku game application.
'''
from gomoku_game import GomokuGame
def main():
    game = GomokuGame()
    while True:
        game.print_board()
        if game.game_over:
            winning_player = 'O' if game.current_player == 'X' else 'X'  # Determine the winning player
            print(f"Player {winning_player} wins!")
            reset = input("Do you want to play again? (y/n): ")
            if reset.lower() == 'y':
                game.reset_game()
                continue
            else:
                break
        try:
            row = int(input(f"Player {game.current_player}, enter your move row (0-14): "))
            col = int(input(f"Player {game.current_player}, enter your move column (0-14): "))
            if 0 <= row < 15 and 0 <= col < 15:  # Validate input range
                game.make_move(row, col)
            else:
                print("Invalid move. Please enter values between 0 and 14.")
        except (ValueError, IndexError):
            print("Invalid move. Please try again.")
if __name__ == "__main__":
    main()