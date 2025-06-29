'''
Main application file for the Extended ABC string checker.
'''
import sys
from abc_checker import is_extended_abc_string
def main():
    '''
    Main function to receive input and check if it's an Extended ABC string.
    '''
    input_string = input("Enter a string (A, B, C): ")
    result = is_extended_abc_string(input_string)
    print(result)
if __name__ == "__main__":
    main()