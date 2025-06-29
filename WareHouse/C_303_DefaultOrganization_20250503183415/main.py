'''
Main entry point for the Takahashi Game application.
'''
from game_logic import TakahashiGame
def main():
    game = TakahashiGame()
    game.start_game()
if __name__ == "__main__":
    main()