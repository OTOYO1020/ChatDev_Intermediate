'''
Main entry point for the Gomoku game application.
'''
from gomoku import GomokuGame
if __name__ == "__main__":
    game = GomokuGame()
    while True:
        game.display_board()
        try:
            x, y = map(int, input(f"Player {game.current_player}, enter your move (row and column separated by space): ").strip().split())
            result = game.make_move(x, y)
            if result:
                game.display_board()
                print(result)
                if "wins" in result:
                    break
        except (ValueError, IndexError):
            print("Invalid move. Please enter valid row and column numbers.")