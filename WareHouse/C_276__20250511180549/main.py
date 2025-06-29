'''
Contains the main logic for the Gomoku game.
'''
from game import GomokuGame  # Import the GomokuGame class
def main():
    game = GomokuGame()  # Create an instance of the game
    while True:
        print(game)  # Display the current board
        try:
            x, y = map(int, input(f"Player {game.current_player}, enter your move (row and column): ").split())
            if not game.make_move(x, y):
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")
            continue
        if game.winner:
            print(f"Player {game.winner} wins!")
            break
        if game.is_draw():
            print("The game is a draw!")
            break
    if input("Do you want to play again? (y/n): ").lower() == 'y':
        game.reset_game()
        main()  # Restart the game
if __name__ == "__main__":
    main()  # Start the game