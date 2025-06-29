'''
Main entry point for the Gomoku game application.
'''
from gomoku_game import GomokuGame
def main():
    game = GomokuGame()
    while True:
        print(game)
        try:
            row = int(input(f"Player {game.current_player}, enter your move row (0-14): "))
            col = int(input(f"Player {game.current_player}, enter your move column (0-14): "))
            result = game.make_move(row, col)
            if result:
                print(result)  # Inform the user of the game result
                print(game)  # Show final board state
                break  # End game if there's a winner or a draw
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 14.")
        except IndexError:
            print("Invalid move. Please enter numbers between 0 and 14.")
if __name__ == "__main__":
    main()