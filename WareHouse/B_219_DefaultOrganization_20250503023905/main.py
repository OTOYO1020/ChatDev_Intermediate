'''
Main application file for the string concatenation program.
'''
def get_valid_input(prompt, validation_func, error_message):
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        print(error_message)
def is_valid_s1(s): 
    return bool(s)  # S1 cannot be empty
def is_valid_s2(s): 
    return bool(s)  # S2 cannot be empty
def is_valid_s3(s): 
    return bool(s)  # S3 cannot be empty
def is_valid_t(t): 
    return bool(t) and all(char in '123' for char in t)  # T must be valid
def main():
    # Read inputs from standard input
    s1 = get_valid_input("Enter string S1: ", is_valid_s1, "S1 cannot be empty.")
    s2 = get_valid_input("Enter string S2: ", is_valid_s2, "S2 cannot be empty.")
    s3 = get_valid_input("Enter string S3: ", is_valid_s3, "S3 cannot be empty.")
    t = get_valid_input("Enter string T (composed of 1, 2, 3): ", is_valid_t, "T must only contain the characters 1, 2, or 3.")
    result = []
    # Loop through each character in T
    for char in t:
        if char == '1':
            result.append(s1)
        elif char == '2':
            result.append(s2)
        elif char == '3':
            result.append(s3)
    # Concatenate all strings in the result list
    final_string = ''.join(result)
    # Print the final concatenated string
    print(final_string)
if __name__ == "__main__":
    main()