'''
Main application file for the tournament system.
'''
import sys
from tournament_logic import find_second_place
def main():
    try:
        n = int(input("Enter number of players (N): "))
        if n < 0:
            raise ValueError("N must be a non-negative integer.")
        num_players = 2 ** n
        if num_players > 1024:
            raise ValueError("N must be such that 2^N is a valid number of players (e.g., <= 1024).")
        ratings_input = input("Enter player ratings (comma-separated): ")
        ratings = list(map(int, ratings_input.split(',')))
        if len(ratings) != num_players:
            raise ValueError(f"Number of ratings must be {num_players}.")
        second_place = find_second_place(n, ratings)
        print(f"The second place player is: {second_place}")
    except ValueError as ve:
        print(f"Input Error: {str(ve)}", file=sys.stderr)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
if __name__ == "__main__":
    main()