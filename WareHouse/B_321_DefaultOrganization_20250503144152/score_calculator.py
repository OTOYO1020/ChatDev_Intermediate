'''
Score calculation module for the score calculator.
'''
class ScoreCalculator:
    def calculate_min_score_needed(self, n, x, scores):
        scores.sort()
        if n == 3:
            # When N = 3, the current sum is simply the middle score
            current_sum = scores[1]
        else:
            # For N > 3, sum the scores from index 1 to N-2
            current_sum = sum(scores[1:n-1])
        highest_score = scores[-1]
        lowest_score = scores[0]
        # Check if all scores are the same
        if highest_score == lowest_score:
            if current_sum < x:
                return -1  # Impossible to achieve the required grade
            elif current_sum >= x:
                return 0  # No additional score needed
        # Calculate the required total score
        required_total = x + (highest_score + lowest_score)
        # Compute the minimum score needed in round N
        min_score_needed = required_total - current_sum
        # Check if the minimum score needed is within the valid range
        if min_score_needed < 0:
            return 0
        elif min_score_needed > 100:
            return -1  # Impossible to achieve the required grade
        else:
            return min_score_needed