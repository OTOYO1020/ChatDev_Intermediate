'''
Main application file for the character replacement tool.
'''
import re  # Import regex for better input validation
def replace_characters(input_string, char_pairs):
    """
    Replace all occurrences of specified characters in the input string.
    Parameters:
    input_string (str): The original string to modify.
    char_pairs (list of tuples): A list of character pairs (c, d) where c is replaced by d.
    Returns:
    str: The modified string after all replacements.
    """
    for c, d in char_pairs:
        input_string = input_string.replace(c, d)
    return input_string
def main():
    N = int(input("Enter the length of the string: "))
    Q = int(input("Enter the number of character pairs: "))
    S = input("Enter the string of length N: ")
    # Validate the length of the input string
    if len(S) != N:
        print(f"Error: The length of the input string must be {N}.")
        return
    char_pairs = []
    for _ in range(Q):
        pair = input("Enter character pair in the format (c,d): ").strip()
        # Validate the input format
        if re.match(r'^\(\w,\w\)$', pair):
            c, d = pair[1], pair[3]  # Extract characters from the input
            char_pairs.append((c, d))
        else:
            print("Error: Please enter a valid character pair in the format (c,d).")
            return
    modified_string = replace_characters(S, char_pairs)
    print("Modified String:", modified_string)
if __name__ == "__main__":
    main()