'''
Main application file for the Cost Calculator.
'''
import math  # Importing math module to use math.inf
from cost_calculator import calculate_cost  # Importing the calculate_cost function from the module
def main():
    try:
        N = int(input("Enter the total number of items (N): "))
        A = int(input("Enter the divisor for the first operation (A): "))
        X = int(input("Enter the cost for the first operation (X): "))
        Y = int(input("Enter the cost for the second operation (Y): "))
        # Input validation
        if N < 0 or A <= 0 or X < 0 or Y < 0:
            print("Please enter valid non-negative integers for N, X, Y and a positive integer for A.")
            return
        min_cost = calculate_cost(N, A, X, Y)  # Calculate the minimum expected cost
        print(f"Minimum Expected Cost: {min_cost}")
    except ValueError:
        print("Please enter valid integers.")
if __name__ == "__main__":
    main()