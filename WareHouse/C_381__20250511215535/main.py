'''
Main entry point for the Gomoku game application.
'''
from gomoku import GomokuGame
if __name__ == "__main__":
    game = GomokuGame()
    while True:
        game.display_board()
        try:
            row = int(input(f"Player {game.current_player}, enter your move row (0-14): "))
            col = int(input(f"Player {game.current_player}, enter your move column (0-14): "))
            result = game.make_move(row, col)
            if result:
                game.display_board()
                print(result)
                if "wins" in result or "Game over" in result:
                    break
        except (ValueError, IndexError):
            print("Invalid move. Please enter row and column values between 0 and 14.")