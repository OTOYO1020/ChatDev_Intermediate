'''
Main application file for the LexicoSorter application.
'''
from sorter import LexicoSorter
def main():
    while True:
        try:
            print("Please enter a string between 1 and 200,000 characters:")  # Added instruction
            user_input = input()
            if validate_input(user_input):
                sorter = LexicoSorter()
                sorted_string = sorter.sort(user_input)
                print(sorted_string)
                break  # Exit the loop after successful sorting
            else:
                print("Please try again.")  # Prompt for re-entry
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")  # Prompt for re-entry after an error
def validate_input(input_string):
    # Strip whitespace and validate the length of the input string
    input_string = input_string.strip()
    if isinstance(input_string, str) and len(input_string) > 0 and len(input_string) <= 200000:
        return True
    else:
        print("Input must be a non-empty string between 1 and 200,000 characters.")
        return False
if __name__ == "__main__":
    main()