'''
Utility functions for checking subsequences.
'''
def is_subsequence(s: str, t: str) -> bool:
    '''
    Checks if string t is a subsequence of string s.
    '''
    it = iter(s)
    return all(char in it for char in t)
def find_minimum_i(s: str, t: str) -> int:
    '''
    Determines the minimum integer i such that t is a subsequence of the first i characters of the concatenated string s.
    '''
    len_s = len(s)
    len_t = len(t)
    char_positions = {}
    # Create a mapping of character positions in s
    for index, char in enumerate(s):
        if char not in char_positions:
            char_positions[char] = []
        char_positions[char].append(index)
    total_chars_processed = 0
    current_position = 0  # Start from the first character of the first copy of s
    for char in t:
        if char not in char_positions:
            return -1  # Character not found in s
        positions = char_positions[char]
        found = False
        # Search for the next valid position
        while current_position // len_s < len_t:  # While we haven't processed all characters in t
            effective_index = current_position % len_s
            if effective_index in positions:
                found = True
                break
            total_chars_processed += len_s
            current_position += len_s  # Move to the next copy of s
        if not found:
            return -1  # If still not found, return -1
        # Move to the next character in t
        current_position += 1  # Move to the next character in the concatenated string
    return total_chars_processed + current_position  # Return the total processed characters