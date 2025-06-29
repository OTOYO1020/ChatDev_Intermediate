'''
Main application file for the string transformation.
'''
from transform import f, count_operations
def main():
    input_str = input("Enter a string of digits (1-9): ")
    if validate_input(input_str):
        result = count_operations(input_str)
        if result == -1:
            print("Infinite operations detected or output exceeds limit.")
        else:
            print(f"Number of operations: {result}")
    else:
        print("Input must be digits from 1 to 9 and length between 2 and 10^6.")
def validate_input(input_str):
    """
    Validates the input string to ensure it contains only digits from '1' to '9'
    and has a length between 2 and 10^6.
    Args:
    input_str (str): The input string to validate.
    Returns:
    bool: True if the input is valid, False otherwise.
    """
    return (input_str.isdigit() and 
            2 <= len(input_str) <= 10**6 and 
            all('1' <= char <= '9' for char in input_str))
if __name__ == "__main__":
    main()