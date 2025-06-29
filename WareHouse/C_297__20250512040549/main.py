'''
Main application file for the string replacement application.
'''
from string_processor import max_pcs
def main():
    # Prompt the user to enter strings, one per line
    input_text = input("Enter strings (one per line, end with an empty line):\n")
    input_lines = []
    # Collect input lines until an empty line is entered
    while input_text:
        input_lines.append(input_text)
        input_text = input()
    # Determine the number of strings
    H = len(input_lines)
    # Set a constant maximum length for validation
    W = 100  # Example maximum length, adjust as necessary
    # Input validation
    if H == 0:
        print("No strings were entered.")
        return
    if any(len(s) > W for s in input_lines):
        print("One or more strings exceed the maximum length specified.")
        return
    # Process the strings to replace 'TT' with 'PC'
    modified_strings = max_pcs(H, W, input_lines)
    # Output the modified strings
    print("\nOutput:")
    for modified_string in modified_strings:
        print(modified_string)
if __name__ == "__main__":
    main()