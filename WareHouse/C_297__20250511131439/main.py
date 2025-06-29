'''
Main file for the Gomoku game application.
'''
from game import GomokuGame
def main():
    game = GomokuGame()
    while True:
        print(game)  # Display the current board
        x = int(input("Enter row (0-14): "))
        y = int(input("Enter column (0-14): "))
        if not game.make_move(x, y):
            print("Invalid move. Try again.")
        if game.game_over:
            print(f"Player {game.current_player} wins!")
            if input("Do you want to play again? (y/n): ").lower() == 'y':
                game.reset_game()
            else:
                break
if __name__ == "__main__":
    main()