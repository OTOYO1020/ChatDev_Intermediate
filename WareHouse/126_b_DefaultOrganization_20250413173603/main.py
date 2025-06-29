'''
Main application file for the numeric string processing.
'''
from converter import convert
def main():
    max_attempts = 3  # Set a limit for user attempts
    attempts = 0
    while attempts < max_attempts:
        numeric_string = input("Enter a 4-digit numeric string (e.g., 1234): ")
        if len(numeric_string) == 4 and numeric_string.isdigit():
            break
        attempts += 1
        print("Input Error: Please enter a valid 4-digit numeric string.")
    else:
        print("Exceeded maximum attempts. Exiting the program.")
        return  # Exit if maximum attempts are reached
    former = numeric_string[:2]
    latter = numeric_string[2:]
    result = convert(former, latter)
    print(result)
if __name__ == "__main__":
    main()