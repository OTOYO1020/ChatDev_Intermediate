'''
Utility functions for the subsequence checking application.
'''
def is_subsequence(s, t):
    '''
    Determines if t is a subsequence of concatenated copies of s.
    Returns the minimum number of copies of s needed or None if not found.
    '''
    if not s:  # Check if s is empty
        return None if t else 0  # If t is also empty, 0 copies are needed
    len_s = len(s)
    len_t = len(t)
    j = 0
    i = 0
    # We will keep looping until we have processed enough characters
    while j < len_t:
        matched = False  # Flag to check if we matched any character in this iteration
        for char in s:
            if j < len_t and char == t[j]:
                j += 1
                matched = True
            if j == len_t:
                return i + 1  # Return the number of copies needed
        i += 1
        # Break if we have processed enough characters
        if not matched and i > (len_t // len_s) + 1:  # Allow for one more iteration
            return None  # If no valid i exists
    return None  # If no valid i exists