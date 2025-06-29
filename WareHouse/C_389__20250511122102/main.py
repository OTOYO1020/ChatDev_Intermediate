'''
Main entry point for the Gomoku game application.
'''
from gomoku_game import GomokuGame
def main():
    play_console()
def play_console():
    game = GomokuGame()
    print("Welcome to Gomoku!")
    print("Players take turns placing their marks (X or O) on a 15x15 board.")
    print("The first player to get 5 in a row (horizontally, vertically, or diagonally) wins.")
    print("Enter your move as two integers: row and column (0-14).")
    while True:
        game.print_board()
        try:
            row = int(input(f"Player {game.current_player}, enter your move row (0-14): "))
            col = int(input(f"Player {game.current_player}, enter your move column (0-14): "))
        except ValueError:
            print("Invalid input, please enter integers only.")
            continue
        if not game.make_move(row, col):
            print("Invalid move, try again.")
            continue
        if game.winner:
            game.print_board()
            print(f"Player {game.winner} wins!")
            if input("Do you want to play again? (y/n): ").lower() == 'y':
                game.reset_game()
            else:
                break
if __name__ == "__main__":
    main()