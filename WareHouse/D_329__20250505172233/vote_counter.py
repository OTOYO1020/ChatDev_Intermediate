'''
VoteCounter class to manage vote counting and determine the winner.
'''
class VoteCounter:
    def __init__(self, num_candidates):
        self.vote_count = [0] * num_candidates
        self.current_winner = None
        self.max_votes = 0
    def add_vote(self, candidate):
        # Check if the candidate number is valid
        if 1 <= candidate <= len(self.vote_count):
            self.vote_count[candidate - 1] += 1
            self.update_winner(candidate)
        else:
            raise ValueError(f"Invalid vote for candidate {candidate}. Ignored.")
    def update_winner(self, candidate):
        current_candidate_votes = self.vote_count[candidate - 1]
        # Check if this is the first vote being counted
        if self.current_winner is None:  # Handle the case where no votes have been counted yet
            self.current_winner = candidate
            self.max_votes = current_candidate_votes
        elif current_candidate_votes > self.max_votes:
            self.current_winner = candidate
            self.max_votes = current_candidate_votes
        elif current_candidate_votes == self.max_votes:
            if candidate < self.current_winner:  # Update only if the candidate number is smaller
                self.current_winner = candidate
    def get_current_winner(self):
        return self.current_winner if self.current_winner is not None else "No votes cast yet"