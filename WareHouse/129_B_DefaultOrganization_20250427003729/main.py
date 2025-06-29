'''
Main application file to run the climbing stairs application.
'''
import sys
from climbing_stairs import ClimbingStairs
def main():
    # Input Handling
    try:
        N = int(input("Enter N (total steps): "))
        M = int(input("Enter M (number of broken steps): "))
        if M < 0 or M > N:
            raise ValueError("M must be between 0 and N.")
        while True:
            broken_steps = list(map(int, input(f"Enter exactly {M} unique broken steps (space-separated): ").split()))
            broken_set = set(step for step in broken_steps if 0 <= step <= N)
            if len(broken_set) == M and len(broken_set) == len(broken_steps):
                break  # Valid input, exit the loop
            else:
                print(f"You must enter exactly {M} unique broken steps within the range 0 to {N}. Please try again.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return  # Exit the program on invalid input
    # Create an instance of ClimbingStairs and calculate the ways
    climbing_stairs = ClimbingStairs()
    result = climbing_stairs.countWaysToClimb(N, M, broken_set)  # Pass broken_set instead of broken_steps
    # Output the Result
    print(result)  # Output the number of ways directly
if __name__ == "__main__":
    main()