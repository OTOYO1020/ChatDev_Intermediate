'''
Main entry point for the Gomoku game application.
'''
from gomoku_game import GomokuGame
def main_menu():
    print("Welcome to Gomoku!")
    print("1. Play in Console")
    choice = input("Please select an option (1): ")
    return choice
if __name__ == "__main__":
    choice = main_menu()
    if choice == '1':
        game = GomokuGame()
        while True:
            print(game)
            try:
                x, y = map(int, input(f"Player {game.current_player}, enter your move (row and column): ").split())
                if 0 <= x < 15 and 0 <= y < 15:
                    game.make_move(x, y)
                    if game.winner:
                        print(f"Player {game.winner} wins!")
                        print(game)  # Show final board
                        break
                else:
                    print("Invalid move. Please enter coordinates between 0 and 14.")
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")
    else:
        print("Invalid choice. Please restart the application.")