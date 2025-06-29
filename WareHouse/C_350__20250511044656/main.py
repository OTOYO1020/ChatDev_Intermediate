'''
Main file to run the Gomoku game without GUI.
'''
from game import GomokuGame
def main():
    game = GomokuGame()
    while True:
        game.display_board()
        try:
            x, y = map(int, input(f"Player {game.current_player}, enter your move (row and column separated by space): ").strip().split())
            result = game.make_move(x, y)
            if result:
                game.display_board()
                print(result)
                if "wins" in result:  # Check if the result is a win message
                    break
        except ValueError:
            print("Invalid input. Please enter row and column numbers separated by space.")
if __name__ == "__main__":
    main()