'''
This is the main entry point for the Gomoku game application.
'''
from gomoku import GomokuGame
def main():
    choice = input("Choose your mode: (1) Console (2) GUI: ")
    if choice == '1':
        game = GomokuGame()
        while True:
            game.print_board()
            if game.winner:
                print(f"Player {game.winner} wins!")
                break
            try:
                x, y = map(int, input(f"Current Player: {game.current_player}. Enter your move (row and column): ").split())
                if not (0 <= x < game.board_size and 0 <= y < game.board_size):
                    print("Invalid move! Please enter valid coordinates.")
                    continue
                if not game.make_move(x, y):
                    print("Invalid move! Cell already occupied.")
            except ValueError:
                print("Invalid input! Please enter two integers separated by a space.")
            except IndexError:
                print("Invalid move! Please enter valid coordinates.")
    elif choice == '2':
        print("GUI mode is not implemented in this version.")
    else:
        print("Invalid choice! Please select either 1 or 2.")
if __name__ == "__main__":
    main()