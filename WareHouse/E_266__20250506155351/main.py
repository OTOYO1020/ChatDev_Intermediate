'''
Main entry point for the dice game application.
'''
from game import Game
import sys
def main():
    # Read the maximum number of turns from standard input
    try:
        max_turns = int(input("Enter the maximum number of turns: "))
        game = Game(max_turns)
        expected_score = game.run()
        print(f"Final Expected Score: {expected_score:.2f}")
    except ValueError:
        print("Please enter a valid integer for the maximum number of turns.")
        sys.exit(1)
if __name__ == "__main__":
    main()