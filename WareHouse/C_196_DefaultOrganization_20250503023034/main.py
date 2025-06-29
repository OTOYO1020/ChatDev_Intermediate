'''
Main application file for counting valid integers based on user input.
'''
from utils import count_valid_integers
def main():
    try:
        N = int(input("Enter an integer N: "))
        count = count_valid_integers(N)
        print(count)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
if __name__ == "__main__":
    main()