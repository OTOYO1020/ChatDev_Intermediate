'''
Main application file for the substring formation checker.
'''
from utils import validate_input, can_form_substring
if __name__ == "__main__":
    W = int(input("Enter W (occurrences of 'w'): "))
    B = int(input("Enter B (occurrences of 'b'): "))
    if validate_input(W, B):
        result = can_form_substring(W, B)
        print(result)
    else:
        print("Invalid input. Please ensure 0 ≤ W, B ≤ 100 and W + B ≥ 1.")