'''
Main application file for counting intersecting intervals using standard input and output.
'''
from interval_utils import count_intersecting_intervals
from typing import List, Tuple
import re
def main():
    input_text = input("Enter intervals (t, l, r) separated by semicolons: ")
    try:
        intervals = parse_input(input_text)
        N = len(intervals)
        count = count_intersecting_intervals(N, intervals)
        print(f"Number of intersecting pairs: {count}")
    except Exception as e:
        print(f"Input Error: {str(e)}")
def parse_input(input_text: str) -> List[Tuple[int, int, int]]:
    intervals = []
    # Split input by semicolon to handle multiple intervals
    for item in input_text.split(';'):
        item = item.strip()
        if not item:
            continue  # Skip empty entries
        # Use regex to match the expected format (t, l, r)
        pattern = r'^\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*$'
        match = re.match(pattern, item)
        if not match:
            raise ValueError("Each interval must be in the format 't, l, r' where t is 1 (closed) or 2 (open).")
        t, l, r = map(int, match.groups())
        if t not in (1, 2):  # Validate interval type
            raise ValueError("Interval type must be 1 (closed) or 2 (open).")
        if l > r:  # Validate bounds
            raise ValueError("Left bound must be less than or equal to right bound.")
        intervals.append((t, l, r))
    return intervals
if __name__ == "__main__":
    main()