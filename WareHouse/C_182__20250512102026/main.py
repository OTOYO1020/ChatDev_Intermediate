'''
Main application file for the multiple of 3 checker.
'''
from utils import is_multiple_of_3, min_digits_to_erase
def main():
    '''
    Main function to handle input and output for checking multiples of 3.
    '''
    try:
        N = int(input("Enter a positive integer: "))
        if N <= 0:
            raise ValueError("N must be a positive integer.")
        possible, min_digits = min_digits_to_erase(N)
        if possible:
            print(f"Possible: True, Minimum digits erased: {min_digits}")
        else:
            print("Possible: False, Minimum digits erased: -1")
    except ValueError as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()