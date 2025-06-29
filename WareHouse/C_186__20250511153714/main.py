'''
Main entry point for the Gomoku game application.
'''
from gomoku_game import GomokuGame
def main():
    game = GomokuGame()
    while True:
        print(game)
        if game.winner:
            print(f"Player {game.winner} wins!")
            break  # Exit the loop if there is a winner
        try:
            row = int(input(f"Player {game.current_player}, enter your move (row 0-14): "))
            col = int(input(f"Player {game.current_player}, enter your move (col 0-14): "))
            game.make_move(row, col)
        except ValueError as e:
            print(e)
        except Exception as e:
            print("An unexpected error occurred:", e)
        if input("Do you want to continue playing? (y/n): ").lower() != 'y':
            break
if __name__ == "__main__":
    main()