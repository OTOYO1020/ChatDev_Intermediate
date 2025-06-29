'''
Module to manage user data for AtCoder rating system.
'''
class UserData:
    def __init__(self):
        self.usernames = []
        self.ratings = []
    def add_user(self, username, rating):
        '''
        Adds a user with the given username and rating to the lists.
        '''
        self.usernames.append(username)
        self.ratings.append(rating)
    def get_winner(self):
        '''
        Calculates and returns the username of the winner based on ratings.
        '''
        if not self.usernames:
            return "No users added."  # Return a consistent message if no users are added
        total_rating = sum(self.ratings)
        if total_rating == 0:
            return "No winner, total rating is zero."  # Handle the case where total rating is zero
        user_data = list(zip(self.usernames, self.ratings))
        user_data.sort()  # Sort lexicographically by username
        winner_index = total_rating % len(self.usernames)  # Use len(self.usernames) to ensure it aligns with the number of users
        return user_data[winner_index][0]  # This is safe as winner_index is guaranteed to be valid