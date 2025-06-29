'''
Main file to run the Gomoku game.
'''
from game import GomokuGame
def main():
    main_menu()
def main_menu():
    while True:
        choice = input("Choose game mode: (1) Console, (q to quit): ")
        if choice == '1':
            play_console_game()
        elif choice.lower() == 'q':
            break
        else:
            print("Invalid choice. Please select 1 or q.")
def play_console_game():
    game = GomokuGame()
    while True:
        print(game)
        try:
            x, y = map(int, input(f"Current Player: {game.current_player}. Enter your move (row and column, 0-14): ").split())
            if not (0 <= x < 15 and 0 <= y < 15):
                print("Invalid move. Coordinates are out of bounds (0-14).")
                continue
            game.make_move(x, y)
        except ValueError:
            print("Invalid input. Please enter valid integers for row and column (0-14).")
            continue
        if game.winner:
            print(game)
            print(f"Player {game.winner} wins!")
            if input("Do you want to play again? (y/n): ").lower() != 'y':
                break
            game.reset_game()
        elif game.is_board_full():
            print(game)
            print("The game is a draw!")
            if input("Do you want to play again? (y/n): ").lower() != 'y':
                break
            game.reset_game()
if __name__ == "__main__":
    main()