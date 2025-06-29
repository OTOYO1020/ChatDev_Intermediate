'''
Main entry point for the Bomb Explosion application.
'''
import sys
from board import Board
def main():
    try:
        # Read the dimensions of the board
        R, C = map(int, input().strip().split())
        board_input = [input().strip() for _ in range(R)]
        # Validate the input dimensions
        if len(board_input) != R or any(len(line) != C for line in board_input):
            raise ValueError("Invalid board dimensions.")
        # Initialize the board and populate it
        board = Board(R, C)
        board.populate_board(board_input)
        # Simulate explosions and get the result
        result = board.explode_bombs()
        # Print the final state of the board
        for line in result:
            print(line)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
if __name__ == "__main__":
    main()