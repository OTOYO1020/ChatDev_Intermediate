'''
Main application file for AtCoder user rating system.
'''
import sys
from user_data import UserData  # Importing UserData class
def main():
    N = int(input("Enter the number of AtCoder users: "))  # User-friendly prompt
    if N <= 0:
        print("No users to process.")
        return  # Exit the program if there are no users
    app = UserData()  # Using UserData class
    for _ in range(N):
        user_input = input("Enter username and rating (separated by space, e.g., 'user1 1500'): ")
        try:
            username, rating = user_input.split()
            rating = int(rating)
            app.add_user(username, rating)
        except ValueError:
            print("Invalid input. Please enter a username followed by a valid integer rating.")
            continue
    winner = app.get_winner()
    print(winner)  # Print the winner's username directly
if __name__ == "__main__":
    main()