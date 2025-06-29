'''
Main application file for the Takahashi game.
'''
import sys
from game_logic import can_play, play_game
from input_handler import load_words
from output_handler import display_results
def main():
    try:
        N = int(input("Enter number of words: "))
        words = load_words(N)
        results = []
        for word in words:
            winner = play_game(word, words, set())
            results.append(winner)
        display_results(results)
    except ValueError:
        print("Please enter a valid number.")
if __name__ == "__main__":
    main()