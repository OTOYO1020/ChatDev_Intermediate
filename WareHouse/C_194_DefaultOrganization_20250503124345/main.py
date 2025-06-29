'''
Main application file for the Sum of Squared Differences Calculator.
'''
from calculations import calculate_sum_squared_differences
def main():
    # Read the integer N from standard input
    N = int(input())
    # Read the sequence of integers A from standard input
    sequence = list(map(int, input().split()))
    # Validate the length of the sequence
    if len(sequence) != N:
        raise ValueError("The length of the sequence does not match N.")
    # Calculate the sum of squared differences
    result = calculate_sum_squared_differences(N, sequence)
    # Print the result
    print(result)
if __name__ == "__main__":
    main()