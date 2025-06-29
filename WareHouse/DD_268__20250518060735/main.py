'''
Main entry point of the Username Finder application.
'''
from itertools import permutations
from typing import List
class UsernameGenerator:
    def find_username(self, N: int, S: List[str], M: int, T: List[str]) -> str:
        '''
        Generate all permutations of strings in S, concatenate them, and check for valid usernames.
        '''
        if N <= 0 or M < 0 or not S or not T:  # Validate inputs
            return '-1'
        for perm in permutations(S):
            username = '_'.join(perm)  # Form the username first
            username_length = len(username)  # Calculate the length of the concatenated username
            # Adjust the length check to account for underscores
            if username_length < 3 or username_length > 16:
                continue  # Skip this username if it is less than 3 or exceeds 16 characters
            if self.is_valid_username(username, T):
                return username
        return '-1'
    def is_valid_username(self, username: str, taken_usernames: List[str]) -> bool:
        '''
        Check if the generated username is valid (not in the list of taken usernames).
        '''
        return username not in taken_usernames
if __name__ == "__main__":
    # Example usage
    N = 3
    S = ["user", "name", "test"]
    M = 2
    T = ["user_name", "test_user"]
    generator = UsernameGenerator()
    valid_username = generator.find_username(N, S, M, T)
    print(valid_username)