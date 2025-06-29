'''
Main application file for the Twin Good Integers Finder.
'''
from utils import digit_sum, is_good_integer, find_twin_good_integers
def main():
    try:
        N = int(input("Please enter a positive integer (N): "))  # Clarified prompt
        if N <= 0:
            raise ValueError("N must be a positive integer.")
        result = find_twin_good_integers(N)
        if isinstance(result, str):  # Check if the result is a string message
            print(result)
        else:
            print(f"Twin Good Integers found: {result}")  # Improved output message
    except ValueError as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()