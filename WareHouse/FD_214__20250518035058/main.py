'''
Main entry point of the application that handles input and output.
'''
from string_counter import count_possible_strings
if __name__ == "__main__":
    S = input("Enter a string (1-200,000 characters): ")
    if 1 <= len(S) <= 200000:
        marked_chars_input = input("Enter marked characters (e.g., 'ab'): ")
        marked_chars = set(marked_chars_input)  # Convert input to a set of marked characters
        result = count_possible_strings(S, marked_chars)  # Call the function with S and marked_chars
        print(f"Possible strings: {result}")
    else:
        print("String length must be between 1 and 200,000 characters.")