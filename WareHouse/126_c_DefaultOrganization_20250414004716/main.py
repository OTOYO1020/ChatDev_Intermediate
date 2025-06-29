'''
Main application file for the probability calculator.
'''
from utils import num_twice


def main():
    '''
    Main function to calculate the probability based on user input.
    '''
    while True:
        try:
            N, K = map(int, input().split())
            if N <= 0 or K <= 0:
                raise ValueError("Both N and K must be natural numbers greater than zero.")
            break  # Exit the loop if input is valid
        except ValueError as e:
            print(f"Input Error: {e}. Please enter valid natural numbers.")
    probability = 0
    for i in range(1, N + 1):
        num = num_twice(i, K)
        probability += (1 / N) * (1 / 2) ** num
    print(probability)  # Output the probability as a plain number
if __name__ == "__main__":
    main()