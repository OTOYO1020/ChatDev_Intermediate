'''
Main entry point for the Gomoku game application.
'''
from gomoku_game import GomokuGame
def main():
    game = GomokuGame()
    while True:
        game.display_board()
        while True:
            user_input = input(f"Player {game.current_player}, enter your move (row and column separated by space) or type -1 to exit: ").strip()
            if user_input == "-1":
                print("Exiting the game.")
                return
            try:
                x, y = map(int, user_input.split())
                if 0 <= x < 15 and 0 <= y < 15:
                    break  # Valid input, exit the inner loop
                else:
                    print("Invalid move! Coordinates are out of bounds. Please enter values between 0 and 14.")
            except ValueError:
                print("Invalid input! Please enter valid row and column numbers separated by space.")
        result = game.make_move(x, y)
        if result:
            print(result)
            game.display_board()
            if "wins" in result:
                play_again = input("Do you want to play again? (y/n): ").strip().lower()
                if play_again == 'y':
                    game.reset_game()
                else:
                    break
if __name__ == "__main__":
    main()