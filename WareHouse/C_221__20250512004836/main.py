'''
Main application file for calculating the maximum product of two integers formed by permuting the digits of a given integer.
'''
from utils import max_product_of_separated_integers
def main():
    '''
    Main function to execute the maximum product calculation.
    '''
    user_input = input("Enter a positive integer: ")
    try:
        N = int(user_input)
        if N <= 0:
            raise ValueError("Input must be a positive integer.")
        max_product = max_product_of_separated_integers(N)
        print(f"Max Product: {max_product}")
    except ValueError as e:
        print(f"Invalid input: {e}")
if __name__ == "__main__":
    main()