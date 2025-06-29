'''
Main application file for the Interval Game.
'''
from typing import List, Tuple
from game_logic import determine_winner
def parse_intervals(input_text: str) -> List[List[Tuple[int, int]]]:
    """
    Parse the input string to extract test cases and their intervals.
    """
    test_cases = []
    for case in input_text.split('|'):
        intervals = []
        for interval in case.split(';'):
            L, R = map(int, interval.split(','))
            if L >= R:
                raise ValueError(f"Invalid interval: [{L}, {R}) must have L < R.")
            intervals.append((L, R))
        test_cases.append(intervals)
    return test_cases
class IntervalGameApp:
    def __init__(self):
        self.run_app()
    def run_app(self):
        input_text = input("Enter test cases (e.g., '1,2;3,4 | 5,6;7,8'): ")
        if not input_text.strip():
            print("Input Error: Please enter valid intervals.")
            return
        try:
            test_cases = parse_intervals(input_text)
            result = determine_winner(len(test_cases), test_cases)
            print("\n".join(result))
        except ValueError as ve:
            print(f"Input Error: {str(ve)}")
        except Exception as e:
            print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    app = IntervalGameApp()