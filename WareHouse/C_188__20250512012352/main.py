'''
Main application file for the tournament application.
'''
import sys
from tournament import find_second_place
def main():
    try:
        N = int(input("Enter number of players (1-16): "))
        ratings = list(map(int, input("Enter player ratings (comma-separated): ").split(',')))
        if validate_input(N, ratings):
            second_place_label = find_second_place(N, ratings)
            print(f"Second Place Player: {second_place_label}")
        else:
            print("Invalid input. Please ensure N is between 1 and 16 and ratings are unique integers.")
    except ValueError:
        print("Please enter valid integers.")
def validate_input(N, ratings):
    return 1 <= N <= 16 and len(ratings) == N and len(set(ratings)) == N and all(1 <= rating <= 10**9 for rating in ratings)
if __name__ == "__main__":
    main()