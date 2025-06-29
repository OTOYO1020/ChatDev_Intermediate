'''
Main application file for the step climbing calculator.
'''
import sys
from logic import countWaysToClimb
def main():
    # Input Handling
    while True:
        try:
            N = int(input("Enter total steps (N): "))
            if N < 0:
                raise ValueError("Total steps (N) must be a non-negative integer.")
            M = int(input("Enter number of broken steps (M): "))
            if M < 0:
                raise ValueError("Number of broken steps (M) must be a non-negative integer.")
            break  # Exit loop if input is valid
        except ValueError as e:
            print(f"Invalid input. Please enter non-negative integers. Error: {e}")
    # Initialize broken_steps based on the value of M
    if M == 0:
        broken_steps = []  # No broken steps
    else:
        while True:
            try:
                broken_steps_input = input("Enter broken steps (comma-separated): ").strip()
                if not broken_steps_input:  # Check for empty input
                    raise ValueError("Broken steps cannot be empty.")
                # Attempt to convert input to a list of integers
                broken_steps = list(map(int, broken_steps_input.split(',')))  # Keep as list for function compatibility
                # Validate broken steps
                for step in broken_steps:
                    if step < 0 or step > N:
                        raise ValueError("Broken steps must be between 0 and N inclusive.")
                broken_steps = list(set(broken_steps))  # Ensure unique broken steps
                break  # Exit loop if input is valid
            except ValueError as e:
                print(f"Invalid input. Please enter integers only, separated by commas. Error: {e}")
    # Calculate the number of ways to climb
    result = countWaysToClimb(N, M, broken_steps)
    # Output the Result
    print(f"Ways to climb: {result}")
if __name__ == "__main__":
    main()