'''
Main application file for the happiness calculator.
'''
import sys
from happiness_calculator import HappinessCalculator
def main():
    try:
        N = int(input("Enter the number of dishes (N): "))
        T = int(input("Enter the time limit (T): "))
        # Enhanced input validation for A
        while True:
            try:
                A = list(map(int, input("Enter the eating times (A) separated by commas (e.g., 1,2,3): ").split(',')))
                break  # Exit loop if input is valid
            except ValueError:
                print("Invalid input for eating times. Please enter integers separated by commas.")
        # Enhanced input validation for B
        while True:
            try:
                B = list(map(int, input("Enter the deliciousness values (B) separated by commas (e.g., 10,20,30): ").split(',')))
                break  # Exit loop if input is valid
            except ValueError:
                print("Invalid input for deliciousness values. Please enter integers separated by commas.")
        # Validate input lengths
        if len(A) != N or len(B) != N or N < 0:
            raise ValueError("The lengths of A and B must match N and N must be non-negative.")
        calculator = HappinessCalculator()
        max_happiness = calculator.max_happiness(N, T, A, B)
        print(f"The maximum happiness is: {max_happiness}")
    except ValueError as ve:
        print(f"Input Error: {ve}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
if __name__ == "__main__":
    main()