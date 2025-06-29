'''
Main application file for the Weight Difference Calculator.
This program calculates the minimum absolute difference between two sums
of weights based on user input.
'''
def calculate_difference(weights):
    """
    Calculate the minimum absolute difference between two sums
    S1 and S2, where S1 is the sum of the first T weights and
    S2 is the sum of the remaining weights.
    Args:
    weights (list): A list of weights (integers).
    Returns:
    int: The minimum absolute difference between S1 and S2.
    """
    N = len(weights)
    total_sum = sum(weights)
    min_difference = float('inf')
    for T in range(1, N):
        S1 = sum(weights[:T])
        S2 = total_sum - S1
        min_difference = min(min_difference, abs(S1 - S2))
    return min_difference
def main():
    """
    Main function to handle user input and display the minimum weight difference.
    It prompts the user for the number of weights and the weights themselves,
    ensuring that all weights are positive integers.
    """
    # Input Handling
    while True:
        try:
            N = int(input("Enter the number of weights: "))
            weights = list(map(int, input(f"Enter {N} positive weights (space-separated): ").split()))
            # Ensure the input is valid
            if len(weights) != N or any(weight <= 0 for weight in weights):
                print("Error: Weights must be positive integers and match the specified count. Please try again.")
                continue
            break  # Exit the loop if input is valid
        except ValueError:
            print("Error: Please enter valid integers for weights. Please try again.")
    # Calculate the minimum difference
    min_difference = calculate_difference(weights)
    # Output Result
    print(f"Minimum Difference: {min_difference}")
if __name__ == "__main__":
    main()