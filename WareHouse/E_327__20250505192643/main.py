'''
Main entry point for the Contest Rating Calculator application.
'''
import sys
from contest_rating_calculator import ContestRatingCalculator
def main():
    '''
    Reads input from standard input, calculates the maximum rating, and prints the result.
    '''
    try:
        # Read the number of contests
        N = int(input("Enter the number of contests: "))
        if N < 1:
            print("Number of contests must be at least 1.")
            return
        # Read the performance values
        performances = list(map(int, input("Enter performance values (space-separated): ").split()))
        if len(performances) != N:
            print(f"Expected {N} performance values, but got {len(performances)}.")
            return
        # Validate performance values
        for performance in performances:
            if not isinstance(performance, int) or performance < 0 or performance > 3000:
                print(f"Performance values must be integers between 0 and 3000. Invalid value: {performance}")
                return
        calculator = ContestRatingCalculator(performances)
        max_rating = calculator.calculate_max_rating()
        print(f"Max Rating: {max_rating:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()