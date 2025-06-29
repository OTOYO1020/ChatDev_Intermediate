'''
Main entry point for the application that validates a string based on specified rules.
'''
def main():
    input_string = input("Enter a string (1-100 characters): ")
    # Check for valid length of the input string
    if len(input_string) < 1 or len(input_string) > 100:  
        print("Input must be between 1 and 100 characters.")
        return
    is_easily_playable = True
    valid_characters = set('LRUD')  # Define the set of valid characters
    for index, char in enumerate(input_string):
        if char not in valid_characters:  # Check for invalid characters
            print("Input contains invalid characters.")
            return
        if index % 2 == 0:  # Even index (0, 2, 4, ...)
            if char not in 'LUD':  # Check for valid characters ('L', 'U', 'D') at even indices
                is_easily_playable = False
                break
        else:  # Odd index (1, 3, 5, ...)
            if char not in 'RUD':  # Check for valid characters ('R', 'U', 'D') at odd indices
                is_easily_playable = False
                break
    # Prepare the result based on the boolean flag
    result = "Yes" if is_easily_playable else "No"
    print(result)
if __name__ == "__main__":
    main()