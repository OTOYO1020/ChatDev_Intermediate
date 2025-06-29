'''
Main entry point for the Gomoku game application.
'''
from board import Board, Cell
def main():
    while True:
        board = Board()
        while True:
            board.display()
            try:
                if board.game_over:
                    print("The game has already ended. Please restart to play again.")
                    break
                row = int(input(f"Player {board.current_player}, enter your row (0-14): "))
                col = int(input(f"Player {board.current_player}, enter your column (0-14): "))
                if 0 <= row < 15 and 0 <= col < 15:  # Input validation
                    if board.make_move(row, col):
                        if board.check_winner():
                            board.display()
                            print(f"Player {board.current_player} wins!")
                            board.game_over = True
                            break
                        if all(cell.state is not None for row in board.cells for cell in row):
                            print("The game is a draw!")
                            board.game_over = True
                            break
                        board.switch_player()
                    else:
                        print("Invalid move, try again.")
                else:
                    print("Invalid input, please enter numbers between 0 and 14.")
            except ValueError:
                print("Invalid input, please enter numbers only.")
        restart = input("Do you want to play again? (y/n): ").strip().lower()
        if restart != 'y':
            break
if __name__ == "__main__":
    main()