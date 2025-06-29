'''
Calculates the longest valid subsequence based on the given constraints.
'''
class SubsequenceCalculator:
    def __init__(self):
        pass
    def longest_valid_subsequence(self, sequence, d):
        max_length = 0
        current_length = 1
        for i in range(1, len(sequence)):
            if abs(sequence[i] - sequence[i - 1]) <= d:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 1
        max_length = max(max_length, current_length)
        return max_length