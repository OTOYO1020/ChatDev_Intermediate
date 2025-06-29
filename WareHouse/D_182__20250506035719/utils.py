'''
Utility functions for input validation and result display.
'''
def validate_input(user_input, expected_length):
    '''
    Validates the user input and returns a list of integers.
    Parameters:
    user_input (str): The input string containing integers separated by spaces.
    expected_length (int): The expected number of integers in the sequence.
    Returns:
    list: A list of integers if the input is valid, None otherwise.
    '''
    if not user_input:  # Check for empty input
        print("Input Error: Input cannot be empty.")
        return None
    try:
        # Trim whitespace and split the input
        sequence = list(map(int, user_input.strip().split()))
        if len(sequence) != expected_length:  # Check for correct length
            print(f"Input Error: Expected {expected_length} elements, but got {len(sequence)}.")
            return None
        return sequence
    except ValueError:
        print("Input Error: Please enter a valid sequence of integers. Ensure all inputs are integers.")
        return None