'''
Main application file for calculating the minimum score needed on the final subject.
'''
import sys
from input_validation import InputValidation
class MainApp:
    def __init__(self):
        self.run()
    def run(self):
        try:
            # Read integers N, K, and M from standard input
            n, k, m = map(int, input().split())
            # Read scores for the first N-1 subjects
            scores = list(map(int, input().split()))
            # Validate inputs
            validator = InputValidation()
            if not validator.validate_inputs(n, k, m, scores):
                return
            required_total = m * n
            current_total = sum(scores)
            needed_score = required_total - current_total
            if needed_score < 0 or needed_score > k:
                print("-1")
            else:
                print(needed_score)
        except ValueError:
            print("Input Error: Please enter valid integers.")
if __name__ == "__main__":
    MainApp()