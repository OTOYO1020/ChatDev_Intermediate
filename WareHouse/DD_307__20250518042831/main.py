'''
Main application file for the string processing.
'''
from utils import remove_contiguous_substrings
if __name__ == "__main__":
    input_string = input("Enter a string (parentheses will be processed): ")
    if not input_string:  # Check for empty input
        print("Input cannot be empty.")
    else:
        modified_string = remove_contiguous_substrings(input_string)
        print(f"Modified String: {modified_string}")