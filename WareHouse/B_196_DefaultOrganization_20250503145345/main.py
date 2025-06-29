'''
Main application file for rounding down a number using standard input and output.
'''
from utils import is_valid_number, round_down_value
def round_down(X):
    """
    Rounds down the input number X after validating it.
    If X is valid, it prints the rounded down result.
    Otherwise, it prints an error message.
    """
    if is_valid_number(X):
        result = round_down_value(X)
        print(result)
    else:
        print("Invalid Input: Please enter a valid number.")
if __name__ == "__main__":
    input_value = input("Enter a number (e.g., 123, -0.5): ")
    round_down(input_value)