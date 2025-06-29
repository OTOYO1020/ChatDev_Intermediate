'''
Main application file for the card game.
'''
import sys
from game_logic import find_winner
def get_number_of_players():
    while True:
        try:
            N = int(input("Enter number of players: "))
            if N <= 0:
                print("Number of players must be a positive integer.")
            else:
                return N
        except ValueError:
            print("Input Error: Please enter a valid integer for the number of players.")
def get_player_data(N):
    colors = []
    ranks = []
    for i in range(N):
        while True:
            try:
                user_input = input(f"Enter color (single word without spaces) and rank (positive integer) for player {i + 1} (separated by space): ")
                parts = user_input.split()
                if len(parts) != 2:
                    raise ValueError("Input must contain exactly two values: color and rank.")
                color, rank = parts
                color = color.strip()  # Trim whitespace
                if not color or ' ' in color:  # Check if color is not empty and does not contain spaces
                    raise ValueError("Color cannot be empty or contain spaces.")
                rank = int(rank)
                if rank <= 0:
                    raise ValueError("Rank must be a positive integer.")
                colors.append(color)
                ranks.append(rank)
                break  # Exit the loop if input is valid
            except ValueError as e:
                print(f"Invalid input. {e} Please enter a valid color followed by a positive integer rank.")
    return colors, ranks
def main():
    N = get_number_of_players()
    colors, ranks = get_player_data(N)
    T = input("Enter color T to check: ").strip()  # Trim whitespace
    if not T or ' ' in T:  # Check if T is not empty and does not contain spaces
        print("Color T cannot be empty or contain spaces.")
        return
    if N > 0:  # Ensure there are players before accessing player 1's color
        winner_id = find_winner(N, colors, ranks, T)
        if winner_id is not None:
            print(f"The winner is Player {winner_id}")
        else:
            print("No winner could be determined based on the provided inputs.")
    else:
        print("No players to determine a winner.")
if __name__ == "__main__":
    main()