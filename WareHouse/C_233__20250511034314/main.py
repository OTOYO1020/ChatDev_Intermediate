'''
This module contains the console version of the Gomoku game.
'''
from gomoku import GomokuGame
def run():
    '''
    Runs the console version of the Gomoku game.
    '''
    while True:
        game = GomokuGame()
        while True:
            game.print_board()
            try:
                row = int(input(f"Player {game.current_player}, enter your move row (0-14): "))
                col = int(input(f"Player {game.current_player}, enter your move column (0-14): "))
                game.make_move(row, col)
                if game.winner:
                    game.print_board()
                    print(f"Player {game.winner} wins!")
                    break
            except (ValueError, IndexError):
                print("Invalid move. Please try again.")
        # Ask if the players want to play again
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            break
if __name__ == "__main__":
    run()