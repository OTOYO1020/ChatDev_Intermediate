'''
Main application file for the string swap counter.
'''
import sys
from count_swaps import count_swaps
def main():
    # Input handling
    string_input = input("Enter String (2-30 characters): ")
    k_input = input("Enter Maximum Swaps (0 to 10^9): ")
    if validate_input(string_input, k_input):
        k = int(k_input)
        result = count_swaps(string_input, k)
        print(f"Number of valid strings: {result}")
    else:
        print("Input Error: Please enter valid inputs.")
def validate_input(string_input, k_input):
    # Validate the length of the string and the value of K
    if not (2 <= len(string_input) <= 30):
        return False
    if not k_input.isdigit() or not (0 <= int(k_input) <= 10**9):
        return False
    return True
if __name__ == "__main__":
    main()