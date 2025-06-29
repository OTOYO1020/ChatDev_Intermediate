'''
Module to manage the vote counting logic.
'''
class VoteCounter:
    '''
    Class to handle vote counting.
    '''
    def __init__(self):
        '''
        Initializes the vote count dictionary.
        '''
        self.vote_count = {}
    def add_vote(self, vote):
        '''
        Updates the vote count for a given string.
        '''
        vote = vote.strip()  # Trim whitespace
        if vote:  # Only count non-empty votes
            if vote in self.vote_count:
                self.vote_count[vote] += 1
            else:
                self.vote_count[vote] = 1
    def get_most_voted(self):
        '''
        Returns the strings with the maximum votes.
        '''
        if not self.vote_count:
            return []
        max_votes = max(self.vote_count.values())
        most_voted_strings = [string for string, count in self.vote_count.items() if count == max_votes]
        most_voted_strings.sort()  # Sort in lexicographical order
        return most_voted_strings