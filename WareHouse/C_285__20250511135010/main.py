'''
Main entry point for the Gomoku game application.
'''
from gomoku_game import GomokuGame
if __name__ == "__main__":
    game = GomokuGame()
    while True:
        game.display_board()
        try:
            x = int(input(f"Player {game.current_player}, enter your move (row 0-14): "))
            y = int(input(f"Player {game.current_player}, enter your move (column 0-14): "))
            result = game.make_move(x, y)
            if result:
                game.display_board()  # Display the board after a win
                print(result)
                game.reset_game()
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 14.")