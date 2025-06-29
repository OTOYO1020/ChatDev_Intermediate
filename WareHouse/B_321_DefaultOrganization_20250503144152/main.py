'''
Main application file for the score calculator.
'''
import sys
from input_validation import InputValidation
from score_calculator import ScoreCalculator
def main():
    # Read inputs from standard input
    n, x = map(int, input().split())
    scores = list(map(int, input().split()))
    # Validate inputs
    validator = InputValidation()
    if not validator.validate_inputs(n, x, scores):
        print("Invalid inputs. Please check your values.")
        return
    # Calculate minimum score needed
    calculator = ScoreCalculator()
    min_score_needed = calculator.calculate_min_score_needed(n, x, scores)
    # Output the result
    if min_score_needed == -1:
        print("It is impossible to achieve the required grade.")
    else:
        print(f"{min_score_needed}")
if __name__ == "__main__":
    main()