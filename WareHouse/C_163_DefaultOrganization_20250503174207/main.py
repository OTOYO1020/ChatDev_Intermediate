'''
Main entry point for the subordinate counting application.
'''
from subordinate_counter import SubordinateCounter
def main():
    while True:
        try:
            n = int(input("Enter number of members (N): "))
            if n < 2:
                raise ValueError("N must be at least 2.")
            bosses = list(map(int, input(f"Enter {n-1} unique bosses (space-separated, each between 1 and {n}): ").split()))
            if len(bosses) != n - 1:
                raise ValueError("Number of bosses must be N-1.")
            # Validate that all bosses are within the valid range and are unique
            if any(boss < 1 or boss > n for boss in bosses):
                raise ValueError(f"All bosses must be between 1 and {n}.")
            if len(set(bosses)) != len(bosses):
                raise ValueError("Bosses must be unique.")
            break  # Exit the loop if input is valid
        except ValueError as e:
            print(f"Input Error: {e}. Please ensure your input is correct.")
            continue  # Continue prompting for input instead of exiting
    counter = SubordinateCounter(n)
    results = counter.count_subordinates(bosses)
    # Print the subordinate counts for each member from 1 to N
    for count in results:  # Print counts for members 1 to N
        print(count)
if __name__ == "__main__":
    main()