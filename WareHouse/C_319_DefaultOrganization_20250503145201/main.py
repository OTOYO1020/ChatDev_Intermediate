'''
Main application file for the 3x3 grid probability calculator.
'''
import itertools
import sys
import math
from grid_validator import GridValidator
from probability_calculator import ProbabilityCalculator
def main():
    grid = []
    print("Please enter the 3x3 grid of integers (9 integers total):")
    for i in range(3):
        try:
            row = list(map(int, input().split()))
            if len(row) != 3:
                print("Each row must contain exactly 3 integers.")
                sys.exit(1)
            grid.append(row)
        except ValueError:
            print("Invalid input. Please enter integers only.")
            sys.exit(1)
    validator = GridValidator(grid)
    if not validator.is_valid():
        print("The grid does not meet the required conditions.")
        return
    disappointment_count = validator.count_disappointments()
    total_permutations = math.factorial(9)  # Calculate total permutations mathematically
    calculator = ProbabilityCalculator(disappointment_count, total_permutations)
    probability = calculator.calculate()
    print(f"Probability of not getting disappointed: {probability:.4f}")
if __name__ == "__main__":
    main()