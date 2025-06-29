'''
Main application file for the Work Days Calculator.
'''
import sys
from workdays import find_work_days
def main():
    # Parse input values from standard input
    input_data = sys.stdin.read().strip().splitlines()
    N = int(input_data[0])  # Total number of days
    K = int(input_data[1])  # Number of workdays to select
    C = int(input_data[2])  # Cooldown period after selecting a workday
    S = input_data[3]       # Availability string for each day
    work_days = find_work_days(N, K, C, S)
    # Format the output as a space-separated string of workdays
    print(" ".join(map(str, work_days)))
if __name__ == "__main__":
    main()