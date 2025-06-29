'''
Input validation module for the score calculator.
'''
class InputValidation:
    def validate_inputs(self, n, x, scores):
        if not (3 <= n <= 100):
            return False
        if not (0 <= x <= 100 * (n - 2)):
            return False
        if len(scores) != n - 1:
            return False
        for score in scores:
            if not (0 <= score <= 100):
                return False
        return True