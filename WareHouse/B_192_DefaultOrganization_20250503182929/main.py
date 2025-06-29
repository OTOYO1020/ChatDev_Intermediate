'''
Main entry point for the Hard-to-Read Checker application.
'''
from string_validator import StringValidator  # Import the StringValidator class
def main():
    input_string = input("Please enter a string (1-1000 characters): ")  # Prompt user for input
    if not input_string:  # Check for empty input
        print("Error: Input cannot be empty.")
        return
    try:
        validator = StringValidator(input_string)  # Create the validator
        result = validator.check_hard_to_read()  # Check if the string is hard to read
        if result:
            print("HARD-TO-READ")
        else:
            print("NOT HARD-TO-READ")
    except ValueError as e:
        print(f"Error: {e}")  # Print the error message if input is invalid
if __name__ == "__main__":
    main()