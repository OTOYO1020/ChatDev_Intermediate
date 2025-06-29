'''
This module contains the command-line interface for the Gomoku game.
'''
from gomoku_game import GomokuGame
def print_board(board):
    for row in board:
        print(' '.join(['.' if cell is None else cell for cell in row]))
def main():
    game = GomokuGame()
    while True:
        print_board(game.board)
        print(f"Player {game.current_player}'s turn")
        try:
            if game.check_winner():  # Check if the game has already been won
                print(f"Game over. Player {game.current_player} has already won!")
                break
            x, y = map(int, input("Enter your move (row and column): ").split())
            result = game.make_move(x, y)
            if result:
                print(result)
                if "wins" in result:  # Only reset the game if there's a win
                    game.reset_game()
        except (ValueError, IndexError):
            print("Invalid move. Please enter row and column as two numbers between 0 and 14.")
if __name__ == "__main__":
    main()