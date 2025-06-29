'''
Module for comparing two strings.
'''
def compare_strings(S, T):
    '''
    Compares two strings S and T and returns the position of the first mismatch
    or the position after the shorter string if they are equal up to that point.
    '''
    # Handle the case where one string is empty
    if S == "" and T == "":
        return 0  # Both strings are equal
    elif S == "":
        return 1  # S is empty, T is not
    elif T == "":
        return 1  # T is empty, S is not
    len_s = len(S)
    len_t = len(T)
    min_length = min(len_s, len_t)
    for i in range(min_length):
        if S[i] != T[i]:
            return i + 1  # Return 1-based index
    if len_s == len_t:
        return 0  # Strings are equal
    elif len_s < len_t:
        return len_s + 1  # S is a prefix of T
    else:
        return len_t + 1  # T is a prefix of S