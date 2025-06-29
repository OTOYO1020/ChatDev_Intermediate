'''
Main application file for the digit erasure calculator.
'''
import sys
from utils import calculate_min_erased
def main():
    while True:
        input_value = input("Enter a positive integer N (only positive integers are accepted): ")
        try:
            n = int(input_value)
            if n <= 0:
                raise ValueError("N must be a positive integer.")
            min_erased = calculate_min_erased(n)
            display_result(min_erased)
            break  # Exit the loop if input is valid
        except ValueError as e:
            print(f"Input Error: {str(e)}. Please try again.")
        except Exception as e:
            print(f"Unexpected Error: {str(e)}. Please enter a valid positive integer.")
def display_result(min_erased):
    if min_erased == -1:
        print("It is not possible to form a multiple of 3.")
    elif min_erased == 0:
        print("No digits need to be erased to form a multiple of 3.")
    else:
        print(f"Minimum digits to erase: {min_erased}")
if __name__ == "__main__":
    main()