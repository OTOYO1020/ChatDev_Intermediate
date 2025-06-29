'''
Main entry point for the Gomoku game application.
'''
from gomoku import GomokuGame
def play_console():
    game = GomokuGame()
    while True:
        game.print_board()
        try:
            row = int(input(f"Player {game.current_player}, enter your move row (0-14): "))
            col = int(input(f"Player {game.current_player}, enter your move column (0-14): "))
            # Check if the move is within the valid range
            if 0 <= row < 15 and 0 <= col < 15:
                if not game.make_move(row, col):  # Check if the move was successful
                    print("Invalid move! Cell already occupied. Please try again.")
                else:
                    if game.winner:
                        game.print_board()
                        print(f"Player {game.winner} wins!")
                        if input("Do you want to play again? (y/n): ").lower() == 'y':
                            game.reset_game()
                        else:
                            break  # Exit the loop if the game is over
            else:
                print("Invalid move. Please enter row and column numbers between 0 and 14.")
        except ValueError:
            print("Invalid input. Please enter valid integers for row and column.")
def main():
    play_console()  # Directly call the console mode as per the user's requirement
if __name__ == "__main__":
    main()