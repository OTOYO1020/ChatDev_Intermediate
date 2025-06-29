'''
This is the main entry point for the Gomoku game application.
'''
from gomoku import GomokuGame  # Import the game logic
def main():
    game = GomokuGame()  # Create a new game instance
    while True:
        game.print_board()  # Print the current board state
        input_command = input("Enter 'reset' to reset the game or 'move' to make a move: ")  # Get input from user
        if input_command == 'reset':
            game.reset_game()
            continue
        try:
            row = int(input("Enter row (0-14): "))  # Get row input from user
            col = int(input("Enter column (0-14): "))  # Get column input from user
            if row < 0 or row > 14 or col < 0 or col > 14:
                print("Invalid input. Please enter values between 0 and 14.")
                continue
            game.make_move(row, col)  # Make the move
            if game.winner:
                game.print_board()  # Print the final board state
                print(f"Player {game.winner} wins!")  # Announce the winner
                break  # Exit the loop if there's a winner
            if all(cell is not None for row in game.board for cell in row):
                game.print_board()  # Print the final board state
                print("It's a draw!")  # Announce the draw
                break  # Exit the loop if the board is full
        except ValueError:
            print("Invalid input. Please enter integers only.")
if __name__ == "__main__":
    main()