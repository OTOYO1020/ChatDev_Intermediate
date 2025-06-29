'''
Main application file for the string processing application.
'''
from string_processor import StringProcessor  # Ensure this line is present
def main():
    input_n = int(input("Enter an integer N: "))  # Read the integer N
    input_str = input("Enter a string: ")  # Read the string S
    if not input_str:
        print("Please enter a string.")
        return
    # Check if N exceeds the length of S
    if input_n > len(input_str):
        print(f"N exceeds the length of the string. Limiting N to {len(input_str)}.")
        input_n = len(input_str)
    # Limit the string to the first N characters
    limited_str = input_str[:input_n]
    processor = StringProcessor()
    result = processor.remove_unmatched_parentheses(limited_str)
    if not result:
        print("No valid characters remain after processing.")
    else:
        print("Result:", result)
if __name__ == "__main__":
    main()