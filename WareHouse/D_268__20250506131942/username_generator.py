'''
Username generation logic for the Username Generator application.
'''
import itertools
class UsernameGenerator:
    '''
    Class to handle the generation of usernames from given strings.
    '''
    def __init__(self, strings, taken_usernames):
        self.strings = [s.strip() for s in strings]
        self.taken_usernames = set(t.strip() for t in taken_usernames)
    def generate_usernames(self):
        '''
        Generate valid usernames based on permutations of the input strings.
        '''
        for perm in self.get_permutations(self.strings):
            candidate = '_'.join(perm)
            if self.is_valid_username(candidate, perm):
                return candidate
        return None
    def get_permutations(self, strings):
        '''
        Get all permutations of the input strings.
        '''
        return itertools.permutations(strings)
    def is_valid_username(self, username, perm):
        '''
        Check if the username is valid based on length and taken usernames.
        '''
        # Create the candidate username by joining the permutation with underscores
        candidate = '_'.join(perm)
        # Calculate the total length considering the underscores
        total_length = len(candidate) + (len(perm) - 1)
        # Check if the length of the concatenated username is within the valid range (3 to 16 characters)
        if total_length < 3 or total_length > 16:
            return False
        # Check if the username is not in the taken usernames (case insensitive)
        return candidate.lower() not in (taken.lower() for taken in self.taken_usernames)