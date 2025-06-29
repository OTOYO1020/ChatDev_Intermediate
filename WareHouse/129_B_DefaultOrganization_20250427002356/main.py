'''
Main application file to run the weight difference calculator.
'''
from weight_calculator import WeightCalculator
def get_weights(weights_input, N):
    attempts = 0
    while attempts < 3:
        try:
            if not weights_input.strip():  # Check for empty input
                raise ValueError("Input cannot be empty. Please enter weights.")
            weights = list(map(int, weights_input.split()))
            if len(weights) != N:
                raise ValueError(f"Expected {N} weights, but got {len(weights)}.")
            if any(weight <= 0 for weight in weights):  # Ensure all weights are positive
                raise ValueError("All weights must be positive integers.")
            return weights
        except ValueError as e:
            attempts += 1
            print(f"Input Error: {e}. Please enter the weights again (1-based index).")
            if attempts < 3:
                weights_input = input("Enter weights separated by spaces: ")
            else:
                print("Maximum attempts reached. Exiting the program.")
                exit(1)  # Exit the program after maximum attempts
def main():
    # Input Handling
    attempts = 0
    while attempts < 3:
        try:
            N = int(input("Enter the number of weights (1-based index): "))
            if N <= 0:
                raise ValueError("The number of weights must be a positive integer.")
            break  # Exit the loop if input is valid
        except ValueError as e:
            attempts += 1
            print(f"Input Error: {e}. Please enter a valid positive integer for N.")
    else:
        print("Maximum attempts reached. Exiting the program.")
        exit(1)  # Exit the program after maximum attempts
    weights = None
    attempts = 0
    while attempts < 3:
        weights_input = input("Enter weights separated by spaces (1-based index): ")
        weights = get_weights(weights_input, N)
        if weights is not None:
            calculator = WeightCalculator(weights)
            min_difference = calculator.calculate_min_difference()
            print(f"Minimum Difference: {min_difference}")
            break  # Exit the loop after successful calculation
        attempts += 1
    else:
        print("Maximum attempts reached. Exiting the program.")
        exit(1)  # Exit the program after maximum attempts
if __name__ == "__main__":
    main()