'''
Module for handling queries and calculating scores.
'''
class QueryHandler:
    def __init__(self, queries):
        self.queries = queries
    def calculate_max_score(self, sequences, N):
        max_score = 0
        # For each sequence, calculate the score based on the queries
        for sequence in sequences:
            score = 0
            for a_i, b_i, c_i, d_i in self.queries:
                # Check if indices are within the valid range
                if 0 <= a_i < N and 0 <= b_i < N:
                    # Ensure b_i is greater than or equal to a_i for valid scoring
                    if b_i >= a_i:
                        # Check the condition for scoring
                        if sequence[b_i] - sequence[a_i] == c_i:
                            score += d_i
            # Update max_score if the current score is greater
            max_score = max(max_score, score)
        return max_score