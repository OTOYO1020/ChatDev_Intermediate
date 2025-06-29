'''
Main application file for AtCoder contest series checker.
'''
from utils import get_remaining_series
def main():
    # Instructions for the user
    print("Please enter three contest series from the following options: 'ABC', 'ARC', 'AGC', 'AHC'")
    valid_series = {'ABC', 'ARC', 'AGC', 'AHC'}
    input_series = []
    attempts = 0
    max_attempts = 10  # Set a maximum number of attempts
    # Loop until we have three valid inputs or max attempts reached
    while len(input_series) < 3 and attempts < max_attempts:
        series = input().strip()
        if series in valid_series:
            if series not in input_series:  # Check for duplicates
                input_series.append(series)
            else:
                print(f"You have already entered '{series}'. Please enter a different contest series.")
        else:
            print(f"Invalid input: '{series}'. Please enter valid contest series.")
        # Provide feedback on how many valid entries are still needed
        if len(input_series) < 3:
            print(f"You still need to enter {3 - len(input_series)} valid contest series.")
        attempts += 1
    # Initialize held series
    held_series = {'ABC', 'ARC', 'AGC', 'AHC'}
    # Get remaining series
    remaining_series = get_remaining_series(input_series, held_series)
    # Prepare result
    if not remaining_series:
        result = "No additional series"
    else:
        result = ", ".join(remaining_series)
    print(result)
if __name__ == "__main__":
    main()