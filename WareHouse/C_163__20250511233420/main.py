'''
This file serves as the entry point for the Gomoku game application.
'''
from gomoku import GomokuGame
def main():
    print("Welcome to Gomoku!")
    game = GomokuGame()
    while True:
        print_board(game.board)
        if game.winner:
            break  # Exit the loop if there is a winner
        try:
            x, y = map(int, input(f"Player {game.current_player}, enter your move (row and column): ").split())
            if 0 <= x < game.board_size and 0 <= y < game.board_size:
                game.make_move(x, y)
            else:
                print("Move out of bounds. Please enter valid coordinates.")
        except (ValueError, IndexError):
            print("Invalid move. Please try again.")
    print(f"Game over! Player {game.winner} has won the game.")  # Display the winner at the end
def print_board(board):
    for row in board:
        print(" ".join(['X' if cell == 1 else 'O' if cell == 2 else '.' for cell in row]))
if __name__ == "__main__":
    main()