'''
Main application file for the string transformation.
'''
def maximize_pcs(strings):
    """
    This function takes a list of strings and replaces occurrences of 'TT' with 'PC'.
    It continues to do this until no more replacements can be made in each string.
    Args:
    strings (list): A list of strings to be modified.
    Returns:
    list: A list of modified strings after all possible replacements.
    """
    modified_strings = []
    for s in strings:
        # Convert string to a list for mutable operations
        s_list = list(s)
        changed = True  # Flag to check if any changes were made
        while changed:
            changed = False  # Reset the flag for this iteration
            i = 0  # Initialize index outside the loop
            while i < len(s_list) - 1:  # Loop until the second last character
                if s_list[i] == 'T' and s_list[i + 1] == 'T':
                    s_list[i] = 'P'
                    s_list[i + 1] = 'C'
                    changed = True  # A change was made, so we need to check again
                    i += 1  # Move to the next character to check for new 'TT'
                i += 1  # Move to the next character
        modified_strings.append(''.join(s_list))  # Append the modified string to the result list
    return modified_strings
if __name__ == "__main__":
    H, W = map(int, input().split())
    strings = []
    for _ in range(H):
        S_i = input().strip()
        strings.append(S_i)
    result = maximize_pcs(strings)
    for modified_string in result:
        print(modified_string)