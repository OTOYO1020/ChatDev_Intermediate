'''
Main application file for the Robot Position Calculator.
'''
from utils import validate_input  # Import the validate_input function
def main():
    '''
    Main function to read input and calculate the maximum position.
    '''
    # Read the number of elements in the sequence with validation
    while True:
        try:
            N = int(input("Enter the number of elements in the sequence: "))
            if N <= 0:
                print("Please enter a positive integer for the number of elements.")
                continue
            break
        except ValueError:
            print("Input Error: Please enter a valid integer for the number of elements.")
    # Read the sequence of integers
    user_input = input(f"Enter {N} integers separated by spaces: ").strip()
    sequence = validate_input(user_input, N)  # Validate the input with expected length
    if sequence is None:  # Check for valid input
        return
    # Initialize variables
    current_position = 0
    max_position = 0
    # Loop through the sequence
    for move in sequence:
        current_position += move
        max_position = max(max_position, current_position)
    # Print the result
    print(max_position)
if __name__ == "__main__":
    main()