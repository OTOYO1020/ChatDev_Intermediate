'''
Main application file for the Username Generator application.
'''
import sys
from username_generator import UsernameGenerator
def main():
    '''
    Main function to handle input and generate usernames.
    '''
    try:
        # Read integers N and M from standard input
        n = int(input())
        strings = [input() for _ in range(n)]
        m = int(input())
        taken = [input() for _ in range(m)]
        # Create a UsernameGenerator instance
        generator = UsernameGenerator(strings, taken)
        # Generate valid usernames
        valid_username = generator.generate_usernames()
        # Output the result
        if valid_username:
            print(valid_username)
        else:
            print("-1")
    except ValueError:
        print("Please enter valid integers for N and M.")
if __name__ == "__main__":
    main()