'''
Main entry point for the Gomoku game application.
'''
from gomoku_game import GomokuGame
def main():
    play_console()
def play_console():
    while True:
        game = GomokuGame()
        while True:
            game.display_board()
            try:
                row = int(input(f"Player {game.current_player}, enter your move row (0-14): "))
                col = int(input(f"Player {game.current_player}, enter your move column (0-14): "))
                if not game.make_move(row, col):
                    continue  # If the move was invalid, prompt for input again
                if game.winner:
                    game.display_board()
                    print(f"Player {game.winner} wins!")
                    break
                if game.is_board_full():
                    game.display_board()
                    print("The game is a draw!")
                    break
            except ValueError:
                print("Invalid input! Please enter integers for row and column.")
        # Ask if players want to play again
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            break
if __name__ == "__main__":
    main()