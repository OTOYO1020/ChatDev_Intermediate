'''
Module for validating user inputs for the score calculator application.
'''
class InputValidation:
    def validate_inputs(self, n, k, m, scores):
        # Check if N, K, and M are within the specified ranges
        if not (1 <= n <= 100) or not (0 <= k <= 100) or not (0 <= m <= 100):
            print("Input Error: N must be between 1 and 100, K and M must be between 0 and 100.")
            return False
        # Check if the number of scores matches N-1
        if len(scores) != n - 1:
            print(f"Input Error: Please enter exactly {n - 1} scores.")
            return False
        # Validate each score to ensure it is within the valid range [0, K]
        for score in scores:
            if not (0 <= score <= k):
                print(f"Input Error: Each score must be between 0 and {k}.")
                return False
        return True