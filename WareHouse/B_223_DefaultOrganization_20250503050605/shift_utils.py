'''
Utility file for performing string left and right shifts.
'''
class ShiftUtils:
    @staticmethod
    def left_shift(s, i):
        '''Returns the left-shifted version of the string s by i positions.'''
        if not s:  # Check for empty string
            raise ValueError("Input string cannot be empty.")
        i = i % len(s)  # Ensure i is within the bounds of the string length
        return s[i:] + s[:i]
    @staticmethod
    def right_shift(s, i):
        '''Returns the right-shifted version of the string s by i positions.'''
        if not s:  # Check for empty string
            raise ValueError("Input string cannot be empty.")
        i = i % len(s)  # Ensure i is within the bounds of the string length
        if i == 0 or i == len(s):  # Handle the case when i is 0 or equal to the length of s
            return s
        return s[-i:] + s[:-i]