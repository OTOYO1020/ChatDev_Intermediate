'''
Main application file for character replacement tool.
'''
def replace_characters(original_string, char_pairs):
    """
    Replace characters in the original string based on the provided pairs.
    Parameters:
    original_string (str): The string in which characters will be replaced.
    char_pairs (list of tuples): A list of tuples containing character pairs (c_i, d_i).
    Returns:
    str: The modified string after all replacements.
    """
    replacements = {}
    for (c_i, d_i) in char_pairs:
        replacements[c_i] = d_i
    modified_string = original_string
    for c_i, d_i in replacements.items():
        modified_string = modified_string.replace(c_i, d_i)
    return modified_string
if __name__ == "__main__":
    # Read integer values N and Q
    N, Q = map(int, input().split())
    # Read the string S of length N
    S = input().strip()
    char_pairs = []
    # Read Q pairs of characters (c_i, d_i)
    for _ in range(Q):
        while True:
            try:
                c_i, d_i = input().strip().split()  # Changed from split(',') to split()
                c_i = c_i.strip()
                d_i = d_i.strip()
                if len(c_i) != 1 or len(d_i) != 1:
                    raise ValueError("Both characters must be single characters.")
                char_pairs.append((c_i, d_i))
                break  # exit the loop if input is valid
            except ValueError as e:
                print(f"Error: {e}. Please enter pairs in the format 'c_i d_i'")  # Updated error message
    # Get the modified string
    result = replace_characters(S, char_pairs)
    # Print the modified string
    print(result)