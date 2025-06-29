'''
This script counts verdicts from standard input for multiple test cases.
The user inputs the number of test cases followed by the verdicts,
and the application will print the counts for each verdict type.
It includes error handling for invalid inputs and ensures that the user
can only enter the specified number of verdicts.
'''
def main():
    # Read the number of test cases
    try:
        N = int(input("Enter the number of test cases (positive integer): "))
        if N <= 0:
            print("Number of test cases must be a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return
    # Initialize counters
    count_AC = 0
    count_WA = 0
    count_TLE = 0
    count_RE = 0
    # Read all verdicts
    print(f"Please enter exactly {N} verdicts (valid options: AC, WA, TLE, RE):")
    for i in range(N):
        while True:  # Keep asking for input until a valid verdict is received
            verdict = input().strip()
            if verdict in ['AC', 'WA', 'TLE', 'RE']:
                if verdict == 'AC':
                    count_AC += 1
                elif verdict == 'WA':
                    count_WA += 1
                elif verdict == 'TLE':
                    count_TLE += 1
                elif verdict == 'RE':
                    count_RE += 1
                break  # Exit the loop if a valid verdict is entered
            else:
                print(f"Warning: Unrecognized verdict '{verdict}' encountered. Please enter valid verdicts.")
    # Prepare and print the output
    print(count_AC, count_WA, count_TLE, count_RE)
if __name__ == "__main__":
    main()