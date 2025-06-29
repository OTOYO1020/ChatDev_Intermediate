'''
Main entry point for the Gomoku game application.
'''
from gomoku_game import GomokuGame
if __name__ == "__main__":
    game = GomokuGame()
    while True:
        print("\nCurrent Board:")
        for row in game.board:
            print(' | '.join(row))
        print("\nCurrent Player:", game.current_player)
        valid_move = False
        while not valid_move:
            try:
                row = int(input("Enter row (0-14): "))
                col = int(input("Enter column (0-14): "))
                valid_move = game.make_move(row, col)
                if valid_move:
                    if game.winner:
                        print(f"Player {game.winner} wins!")
                        break
                else:
                    print("Move was not successful. Try again.")
            except ValueError:
                print("Invalid input. Please enter numbers between 0 and 14.")