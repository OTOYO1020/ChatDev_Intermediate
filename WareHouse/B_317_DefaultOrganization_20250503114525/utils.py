'''
Utility functions for the Lost Integer Calculator application.
'''
def validate_input(n_input, a_input):
    '''
    Validates the user input for N and the list of integers.
    Returns a tuple (is_valid, A) where is_valid is a boolean indicating
    if the input is valid, and A is the list of integers if valid.
    '''
    try:
        N = int(n_input)
        if N < 1:
            raise ValueError("N must be a positive integer.")
        A = a_input.split()
        if len(A) != N:
            raise ValueError(f"Expected {N} integers, but got {len(A)}.")
        # Check if all elements in A are positive integers
        for num in A:
            if not num.isdigit():
                raise ValueError(f"Invalid integer value: {num}. Must be a positive integer.")
        A = list(map(int, A))  # Convert to integers after validation
        return True, A  # Return both validation status and the list of integers
    except ValueError as e:
        print(f"Input Error: {str(e)}")
        return False, []  # Return an empty list if validation fails