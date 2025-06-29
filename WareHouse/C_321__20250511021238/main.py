'''
This is the main entry point of the application that initializes the game
and starts the text-based interaction loop.
'''
from gomoku import GomokuGame
def main():
    while True:  # Loop to allow replaying the game
        game = GomokuGame()
        while True:
            game.display_board()
            try:
                x, y = map(int, input(f"Player {game.current_player}, enter your move (row and column): ").split())
                result = game.make_move(x, y)
                if result:
                    game.display_board()
                    print(result)
                    break  # Exit the inner loop if the game is over
            except (ValueError, IndexError):
                print("Invalid move. Please enter row and column numbers between 0 and 14.")
        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break  # Exit the outer loop if the user does not want to play again
if __name__ == "__main__":
    main()