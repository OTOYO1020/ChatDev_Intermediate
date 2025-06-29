'''
Main application file for checking if one string is a prefix of another.
'''
from string_input import StringInput
def check_prefix(s, t):
    '''
    Function to check if string s is a prefix of string t.
    Parameters:
    s (str): The string to check as a prefix.
    t (str): The string to check against.
    Returns:
    str: "YES" if s is a prefix of t, otherwise a descriptive "NO" message.
    '''
    if not s:
        return "NO: S cannot be a prefix of T because S is empty."
    if not t:
        return "NO: T cannot have a prefix because T is empty."
    len_s = len(s)
    len_t = len(t)
    if len_s > len_t:
        return "NO"  # S cannot be a prefix of T if it's longer
    else:
        prefix_t = t[:len_s]  # Extract the prefix of T with the same length as S
        if s == prefix_t:
            return "YES"  # S is a prefix of T
        else:
            return "NO"  # S is not a prefix of T
if __name__ == "__main__":
    string_input = StringInput()
    s, t = string_input.get_strings()  # Use the StringInput class to get strings
    result = check_prefix(s, t)
    print(result)