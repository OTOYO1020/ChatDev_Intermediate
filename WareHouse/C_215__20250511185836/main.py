'''
Main entry point for the Gomoku game application.
'''
from gomoku_game import GomokuGame
def main_menu():
    print("Welcome to Gomoku!")
    print("1. Play Console Version")
    choice = input("Choose an option (1): ")
    if choice == '1':
        play_console()
    else:
        print("Invalid choice. Please select 1.")
        main_menu()
def play_console():
    while True:
        game = GomokuGame()  # Initialize a new game for each round
        while True:
            print(game)
            try:
                x, y = map(int, input(f"Player {game.current_player}, enter your move (row and column separated by space): ").strip().split())
                game.make_move(x, y)
                if game.winner:
                    print(game)
                    print(f"Player {game.winner} wins!")
                    break
            except ValueError:
                print("Invalid input. Please enter two integers separated by space.")
            except IndexError:
                print("Move out of bounds. Please enter valid coordinates.")
            except Exception as e:
                print(f"An error occurred: {e}")
        # Ask if players want to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break
if __name__ == "__main__":
    main_menu()