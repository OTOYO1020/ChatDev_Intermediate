'''
Main application file for the probability calculator using standard input and output.
'''
from utils import calculate_probability


def main():
    # Read input values for N and K
    N, K = map(int, input().split())
    # Validate inputs for N and K
    if N <= 0 or K <= 0:
        raise ValueError("Both N and K must be natural numbers greater than 0.")
    # Calculate the probability
    probability = calculate_probability(N, K)
    # Output the result with conditional formatting
    if probability.is_integer():
        print(int(probability))  # Print as an integer if it's a whole number
    else:
        print(f"{probability}")  # Otherwise, print with six decimal places
if __name__ == "__main__":
    main()