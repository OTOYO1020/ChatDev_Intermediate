'''
Main application file for the numeric string conversion application.
'''
from conversion import convert_logic
def main():
    """Main function to handle user input and call the conversion logic."""
    numeric_string = input("Enter a 4-digit numeric string: ")
    if len(numeric_string) != 4 or not numeric_string.isdigit():
        print("Input Error: Please enter a valid 4-digit numeric string.")
        return
    former = numeric_string[:2]
    latter = numeric_string[2:]
    result = convert_logic(former, latter)
    print(result)
if __name__ == "__main__":
    main()