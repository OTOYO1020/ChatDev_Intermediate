'''
Main application file for merging intervals using standard input and output.
'''
from interval import Interval  # Importing the Interval class
def read_intervals():
    """
    Reads a number of intervals from standard input.
    Returns:
    list of Interval: A list of Interval objects created from user input.
    """
    while True:
        try:
            N = int(input())
            if N <= 0:
                raise ValueError("The number of intervals must be a positive integer.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")
    intervals = []
    for _ in range(N):
        while True:
            try:
                L, R = map(int, input().split(','))
                if L >= R:
                    raise ValueError("The starting point L must be less than the ending point R.")
                intervals.append(Interval(L, R))
                break
            except ValueError as e:
                print(f"Invalid interval format: {e}. Please enter a valid interval.")
    return intervals
def merge_intervals(intervals):
    """
    Merges overlapping intervals in a list of intervals.
    Parameters:
    intervals (list of Interval): A list of Interval objects to be merged.
    Returns:
    list of Interval: A list of merged Interval objects.
    """
    intervals.sort(key=lambda x: (x.start, x.end))
    merged_intervals = []
    for interval in intervals:
        if not merged_intervals or merged_intervals[-1].end <= interval.start:
            merged_intervals.append(interval)
        else:
            merged_intervals[-1].end = max(merged_intervals[-1].end, interval.end)
    return merged_intervals
def display_intervals(merged_intervals):
    """
    Displays the merged intervals in the specified format.
    Parameters:
    merged_intervals (list of Interval): A list of merged Interval objects to display.
    """
    print(len(merged_intervals))
    for interval in merged_intervals:
        print(f"[{interval.start}, {interval.end})")
if __name__ == "__main__":
    intervals = read_intervals()
    merged_intervals = merge_intervals(intervals)
    display_intervals(merged_intervals)