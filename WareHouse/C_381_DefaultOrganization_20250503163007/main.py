'''
Main application file that calculates the maximum length of valid 11/22 substrings.
'''
def calculate_max_length(input_string):
    # Check for empty input
    if not isinstance(input_string, str) or not input_string:
        return 0
    if any(c not in '12/' for c in input_string):  # Check for invalid characters
        return 0  # Return 0 if invalid characters are found
    if input_string.count('/') == 0:
        return 0  # Return 0 if no '/' is found
    max_length = 0
    i = 0
    while i < len(input_string):
        if input_string[i] == '/':
            left = i - 1
            right = i + 1
            # Expand outward while checking for valid 11/22 substring conditions
            while left >= 0 and right < len(input_string):
                # Check if the characters at the left pointer are valid
                if input_string[left] == '1':
                    left -= 1  # Move left pointer outward
                else:
                    break  # Break if a character is not '1'
                # Check if the characters at the right pointer are valid
                if input_string[right] == '2':
                    right += 1  # Move right pointer outward
                else:
                    break  # Break if a character is not '2'
            # Calculate length after the loop
            length = (right - left - 1)  # Correctly calculates the length of the valid substring
            max_length = max(max_length, length)
            # Skip over consecutive '/' characters
            while i + 1 < len(input_string) and input_string[i + 1] == '/':
                i += 1
        i += 1  # Move to the next character
    return max_length
if __name__ == "__main__":
    input_string = input()  # Read input directly from standard input
    max_length = calculate_max_length(input_string)
    print(max_length)  # Print the maximum length found