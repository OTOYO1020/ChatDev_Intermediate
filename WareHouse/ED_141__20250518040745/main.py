'''
Main entry point of the application that handles user input and output.
'''
from substring_finder import max_length_repeated_substring  # Import the function
if __name__ == "__main__":
    input_string = input("Enter a string: ")
    if not input_string or len(input_string) < 2:
        print("Input Error: Please enter a string with at least two characters.")
    else:
        max_length = max_length_repeated_substring(input_string)
        print(max_length)  # Print only the integer value as required