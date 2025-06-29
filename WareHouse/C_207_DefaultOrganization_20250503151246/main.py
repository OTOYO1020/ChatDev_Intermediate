'''
Main application file for the interval intersection checker.
'''
from interval import Interval
def main():
    intervals = []
    while True:
        try:
            num_intervals = int(input("Enter number of intervals: "))
            if num_intervals <= 0:
                raise ValueError("Number of intervals must be positive.")
            break
        except ValueError as e:
            print(f"Input Error: {e}. Please try again.")
    for i in range(num_intervals):
        while True:
            try:
                t, l, r = map(int, input(f"Enter interval {i + 1} (t, l, r) separated by spaces: ").split())
                if t < 1 or t > 4:
                    raise ValueError("t must be between 1 and 4.")
                intervals.append(Interval(t, l, r))
                break
            except ValueError as e:
                print(f"Input Error: {e}. Please try again.")
    count = check_intersections(intervals)
    print(f"Number of intersecting pairs: {count}")
def check_intersections(intervals):
    '''
    Check for intersections between all pairs of intervals.
    Parameters:
        intervals (list): List of Interval objects.
    Returns:
        int: Count of intersecting pairs.
    '''
    count = 0
    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):
            if intervals[i].intersects(intervals[j]):
                count += 1
    return count
if __name__ == "__main__":
    main()