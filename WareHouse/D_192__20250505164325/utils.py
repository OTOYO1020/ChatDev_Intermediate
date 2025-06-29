'''
Utility functions for the base counting application.
'''
def get_greatest_digit(x):
    '''
    Returns the greatest digit found in the string x.
    '''
    greatest_digit = -1
    for char in x:
        if char.isdigit():
            digit = int(char)
            if digit > greatest_digit:
                greatest_digit = digit
    return greatest_digit
def count_valid_bases(x, greatest_digit, m):
    '''
    Counts the valid bases from greatest_digit + 1 to m.
    '''
    count = 0
    # Check if the input contains only valid digit characters
    if any(not char.isdigit() for char in x):
        print("Error: Input contains non-digit characters. Please provide a valid digit string.")
        return 0  # Early exit if invalid characters are found
    # Proceed only if all characters are valid digits
    for n in range(greatest_digit + 1, m + 1):
        # Check if all characters in x are valid for base n
        if all(int(char) < n for char in x):
            try:
                # Attempt to convert the string x to an integer in base n
                converted_value = int(x, base=n)
                if converted_value <= m:
                    count += 1
            except ValueError:
                # Handle the case where conversion fails
                print(f"Invalid conversion for base {n} with input {x}. Skipping this base.")
        else:
            print(f"Skipping base {n} because not all characters are valid for this base.")
    return count