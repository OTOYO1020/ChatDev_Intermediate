'''
Main entry point for the Gomoku game application.
'''
from gomoku_game import GomokuGame
def main_menu():
    print("Welcome to Gomoku!")
    print("1. Play in Console")
    choice = input("Choose an option (1): ")
    return choice
if __name__ == "__main__":
    choice = main_menu()
    if choice == "1":
        game = GomokuGame()
        while True:
            game.print_board()
            try:
                row = int(input(f"Player {game.current_player}, enter your move row (0-14): "))
                col = int(input(f"Player {game.current_player}, enter your move column (0-14): "))
                move_result, game_over_message = game.make_move(row, col)
                if move_result is False:
                    print(game_over_message)  # Provide feedback on invalid move
                elif game_over_message == "Game Over":
                    game.print_board()
                    print(f"Player {game.winner} wins!")
                    break
            except (ValueError, IndexError):
                print("Invalid input. Please enter numbers between 0 and 14.")
    else:
        print("Invalid choice. Please restart the application.")