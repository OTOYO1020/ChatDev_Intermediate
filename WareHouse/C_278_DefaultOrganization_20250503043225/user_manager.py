'''
User management module to handle follow/unfollow/check status operations.
'''
class UserManager:
    def __init__(self, users):
        # Initialize following relationships for all users as empty sets
        self.following = {str(user): set() for user in users}
    def follow(self, user_a, user_b):
        """
        User A follows User B.
        This creates a one-way following relationship.
        """
        user_a, user_b = str(user_a), str(user_b)
        # Ensure both users are in the following dictionary
        if user_a not in self.following:
            self.following[user_a] = set()
        if user_b not in self.following:
            self.following[user_b] = set()
        if user_a == user_b:
            return False  # User cannot follow themselves
        self.following[user_a].add(user_b)  # User A follows User B
        return True  # Follow operation successful
    def unfollow(self, user_a, user_b):
        """
        User A unfollows User B.
        This removes the one-way following relationship.
        """
        user_a, user_b = str(user_a), str(user_b)
        # Ensure both users are in the following dictionary
        if user_a not in self.following:
            self.following[user_a] = set()
        if user_b not in self.following:
            self.following[user_b] = set()
        if user_a == user_b:
            return False  # User cannot unfollow themselves
        if user_b in self.following[user_a]:
            self.following[user_a].remove(user_b)  # Remove User B from User A's following list
            return True  # Unfollow operation successful
        return False  # User was not following
    def check_status(self, user_a, user_b):
        """
        Check if User A is following User B and vice versa.
        Returns "Yes" if both are following each other, otherwise "No".
        """
        user_a, user_b = str(user_a), str(user_b)
        # Ensure both users are in the following dictionary
        if user_a not in self.following:
            self.following[user_a] = set()
        if user_b not in self.following:
            self.following[user_b] = set()
        if user_a == user_b:
            return "No"  # Users are the same
        is_following = user_b in self.following.get(user_a, set())
        is_followed_by = user_a in self.following.get(user_b, set())
        return "Yes" if is_following and is_followed_by else "No"