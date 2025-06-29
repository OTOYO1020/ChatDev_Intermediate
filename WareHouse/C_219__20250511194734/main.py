'''
Contains the main logic for the Gomoku game with mode selection.
'''
from gomoku_game import GomokuGame
def main():
    print("Welcome to Gomoku!")
    mode = input("Choose mode: (1) Console: ")
    if mode == '1':
        game = GomokuGame()
        while True:
            game.display_board()
            print(f"Current Player: {game.current_player}")
            if game.winner:
                print(f"Player {game.winner} wins!" if game.winner != "Draw" else "It's a Draw!")
                break
            try:
                x, y = map(int, input("Enter your move (row and column): ").split())
                if not game.make_move(x, y):
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter row and column as two integers.")
    else:
        print("Invalid selection. Please restart the game.")
if __name__ == "__main__":
    main()