'''
Main application file for the expected wins calculator.
'''
from typing import List, Tuple
from calculations import calculate_expected_wins
def main():
    input_data = input("Enter number of players and matches (format: N followed by pairs of matches):\n")
    try:
        # Parse input data
        lines = input_data.strip().splitlines()
        N = int(lines[0])
        matches = [tuple(map(int, line.split())) for line in lines[1:]]  # Read all lines after the first
        expected_wins = calculate_expected_wins(N, matches)
        print("Expected Wins:", expected_wins)
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()