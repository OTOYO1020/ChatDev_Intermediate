'''
Main application file for the recent positions finder.
'''
import sys
from functions import find_recent_positions
def main():
    '''
    Main function to handle standard input and output.
    '''
    input_text = input("Enter a sequence of positive integers (comma-separated): ")
    try:
        input_list = list(map(int, input_text.split(',')))
        result = find_recent_positions(len(input_list), input_list)
        print("Result:", result)
    except ValueError:
        print("Input Error: Please enter valid positive integers.")
if __name__ == "__main__":
    main()