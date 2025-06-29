'''
Main entry point for the Gomoku game application.
'''
from board import Board
def main():
    game_board = Board()
    game_board.play_game()
if __name__ == "__main__":
    main()