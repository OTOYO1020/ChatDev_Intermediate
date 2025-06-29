'''
Module to find the greatest level of dango strings.
'''
class DangoLevelFinder:
    '''
    Class to find the greatest level of dango strings.
    '''
    def find_greatest_dango_level(self, S: str) -> int:
        '''
        Finds the greatest level of dango string found in the input string S.
        Parameters:
        S (str): The input string containing dango patterns.
        Returns:
        int: The maximum level of dango string found, or -1 if none exists.
        '''
        if len(S) < 3 or len(S) > 200000:  # Check length constraints
            return -1  # Return immediately if constraints are not met
        max_level = -1
        i = 0
        while i < len(S):
            if S[i] == '-':
                start = i
                while i < len(S) and S[i] == '-':
                    i += 1
                end = i
                o_count = 0  # Initialize o_count for each dango string
                for j in range(start + 1, end):  # Count 'o's between '-'
                    if S[j] == 'o':
                        o_count += 1
                if o_count > 0:  # Valid dango string found (at least one 'o')
                    max_level = max(max_level, o_count)
            else:
                i += 1
        return max_level if max_level >= 0 else -1  # Return -1 if no valid dango string found