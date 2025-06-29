'''
Main application file for the Atcoder Swapper.
'''
import sys
from swap_logic import count_swaps
def main():
    '''
    Main function to read input and calculate the number of swaps.
    '''
    input_string = input("Enter a permutation of 'atcoder': ")
    try:
        operations = count_swaps(input_string)
        print(f"Minimum swaps required: {operations}")
    except ValueError as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()