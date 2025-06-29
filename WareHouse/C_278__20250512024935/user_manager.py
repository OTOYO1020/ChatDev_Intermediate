'''
UserManager class to manage user follow/unfollow relationships.
'''
class UserManager:
    def __init__(self, N):
        self.N = N  # Store the number of users
        self.user_relationships = {i: set() for i in range(1, N + 1)}  # Initialize with all users
    def follow(self, user_a, user_b):
        '''
        Add user_a to the following list of user_b.
        '''
        if not (1 <= user_a <= self.N and 1 <= user_b <= self.N):  # Validate user IDs
            raise ValueError(f"Invalid user IDs: {user_a}, {user_b}")
        self.user_relationships[user_b].add(user_a)
    def unfollow(self, user_a, user_b):
        '''
        Remove user_a from the following list of user_b.
        '''
        if not (1 <= user_a <= self.N and 1 <= user_b <= self.N):  # Validate user IDs
            raise ValueError(f"Invalid user IDs: {user_a}, {user_b}")
        self.user_relationships[user_b].discard(user_a)
    def check_mutual(self, user_a, user_b):
        '''
        Check if user_a and user_b are following each other.
        Returns True if both users follow each other, otherwise False.
        '''
        if not (1 <= user_a <= self.N and 1 <= user_b <= self.N):  # Validate user IDs
            raise ValueError(f"Invalid user IDs: {user_a}, {user_b}")
        follows_a = user_b in self.user_relationships[user_a]  # Check if user_a follows user_b
        follows_b = user_a in self.user_relationships[user_b]  # Check if user_b follows user_a
        return follows_a and follows_b