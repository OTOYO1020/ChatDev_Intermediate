'''
Main entry point for the Palindrome Checker application.
'''
from palindrome_checker import check_palindrome
def main():
    while True:
        try:
            number = int(input("Enter a non-negative integer: ").strip())
            if number < 0:  # Check for negative integers
                print("Invalid input. Please enter a non-negative integer.")
                continue  # Prompt again
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    result = check_palindrome(number)  # Pass the integer directly
    print(result)
if __name__ == "__main__":
    main()