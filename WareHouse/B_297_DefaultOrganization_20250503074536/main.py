'''
Main application file for the string validation.
'''
from validator import validate_input
def main():
    '''
    Main function to run the string validation.
    '''
    input_string = input("Enter a string of length 8 consisting of exactly one 'K', one 'Q', two 'R's, two 'B's, and two 'N's: ")
    result = validate_input(input_string)
    print(result)
if __name__ == "__main__":
    main()