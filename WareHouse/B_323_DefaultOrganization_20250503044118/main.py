'''
Main application file for the player ranking system.
'''
import sys
from utils import count_wins
def main():
    '''
    Main function to execute the player ranking system.
    '''
    while True:
        try:
            n = int(input("Enter the number of players (positive integer): "))
            if n <= 0:
                print("Number of players must be greater than zero.")
                continue  # Prompt again
            break  # Valid input, exit loop
        except ValueError:
            print("Please enter a valid positive integer.")
    results = []
    for i in range(n):
        result = input(f"Enter match results for player {i + 1} (string of 'o' for wins and 'x' for losses): ")
        if not result:  # Check for empty input
            print("Match results cannot be empty.")
            return
        if any(char not in 'ox' for char in result):
            print("Match results can only contain 'o' for wins and 'x' for losses.")
            return
        results.append(result)
    win_counts = count_wins(results)
    players = sorted(enumerate(win_counts, start=1), key=lambda x: (-x[1], x[0]))
    ranked_players = [player[0] for player in players]
    print("Ranked Players:", ranked_players)
if __name__ == "__main__":
    main()