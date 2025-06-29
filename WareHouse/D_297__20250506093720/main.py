'''
Main application file for the integer operation calculator.
'''
from utils import validate_input  # Import the validate_input function
def main():
    '''
    Main function to read input and calculate operations until A equals B.
    '''
    while True:  # Loop until valid input is received
        try:
            a = int(input("Enter positive integer A: "))
            b = int(input("Enter positive integer B: "))
            if not validate_input(a, b):  # Use the validate_input function
                raise ValueError("Both numbers must be positive integers.")
            break  # Exit loop if valid input is received
        except ValueError as e:
            print(f"Input Error: {str(e)}. Please try again.")
    count = 0
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
        count += 1
    print(f"Number of operations performed: {count}")
if __name__ == "__main__":
    main()