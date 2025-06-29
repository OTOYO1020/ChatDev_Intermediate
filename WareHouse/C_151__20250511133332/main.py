'''
Main file to run the Gomoku game application.
'''
from game import GomokuGame
def main():
    while True:  # Loop to allow replaying the game
        game = GomokuGame()
        while not game.game_over:
            game.display_board()
            try:
                x, y = map(int, input(f"Player {game.current_player}, enter your move (row and column): ").split())
                result = game.make_move(x, y)
                if result:
                    game.display_board()  # Display the board after a player wins
                    print(result)
                    break  # Exit the inner loop to allow for a new game
                else:
                    print(f"Player {game.current_player}'s turn")
            except (ValueError, IndexError):
                print("Invalid move. Please enter row and column as two integers between 0 and 14.")
        # Ask if players want to play again
        replay = input("Do you want to play again? (y/n): ").strip().lower()
        if replay != 'y':
            break  # Exit the outer loop to end the game
if __name__ == "__main__":
    main()