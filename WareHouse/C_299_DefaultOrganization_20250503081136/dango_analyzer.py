'''
Module for analyzing dango strings.
'''
class DangoStringAnalyzer:
    '''
    Class to analyze the dango string.
    '''
    def __init__(self, s: str):
        '''
        Initializes the analyzer with the string S.
        '''
        self.s = s
    def find_greatest_level(self) -> int:
        '''
        Finds and returns the greatest level of dango string.
        '''
        x = -1
        length = len(self.s)
        for i in range(length):
            if self.s[i] == '-':
                left_count = 0
                right_count = 0
                # Count 'o' characters to the left
                for j in range(i - 1, -1, -1):
                    if self.s[j] == 'o':
                        left_count += 1
                    else:
                        break
                # Count 'o' characters to the right
                for j in range(i + 1, length):
                    if self.s[j] == 'o':
                        right_count += 1
                    else:
                        break
                # Determine the level L
                level = min(left_count, right_count)
                x = max(x, level)
        return x