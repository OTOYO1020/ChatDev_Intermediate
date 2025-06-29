'''
Main entry point for the Interval Merger application.
'''
import ast  # Import ast for safe evaluation
from intervals import union_intervals
def main():
    '''
    Main function to handle user input and output for merging intervals.
    '''
    try:
        input_intervals = ast.literal_eval(input("Enter intervals (e.g., [(1, 3), (2, 4), (5, 7)]): "))
        if not isinstance(input_intervals, list) or not all(isinstance(i, tuple) and len(i) == 2 and isinstance(i[0], int) and isinstance(i[1], int) and i[0] < i[1] for i in input_intervals):
            raise ValueError("Input must be a list of tuples, each containing two integers where the first is less than the second.")
        result = union_intervals(len(input_intervals), input_intervals)
        print(f"Merged Intervals: {result}")
    except Exception as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()