'''
Main application file for the Confusing Time Finder.
'''
import sys
from time_utils import is_confusing_time, increment_time
def main():
    while True:
        try:
            h = int(input("Enter Hours (0-23): "))
            m = int(input("Enter Minutes (0-59): "))
            if not (0 <= h < 24) or not (0 <= m < 60):
                raise ValueError("Invalid time input. Please enter hours between 0-23 and minutes between 0-59.")
            break  # Exit loop on valid input
        except ValueError as e:
            print(f"Input Error: {str(e)}. Please try again.")
    # Safeguard against infinite loops
    max_iterations = 1440  # Maximum number of minutes in a day
    iterations = 0
    while iterations < max_iterations:
        if is_confusing_time(h, m):
            print(f"Next Confusing Time found: {h}:{m:02d} (This time is confusing!)")
            break
        h, m = increment_time(h, m)
        iterations += 1
    else:
        print("No confusing time found within a day.")
if __name__ == "__main__":
    main()