'''
Main application file for calculating the minimum absolute difference between two groups of weights.
'''
def calculate_min_difference(weights):
    """
    Calculate the minimum absolute difference between the sums of two groups of weights.
    Args:
    weights (list): List of weights indexed from 1 to N (0-indexed in implementation).
    Returns:
    int: Minimum absolute difference between the two groups.
    """
    total_sum = sum(weights)
    min_difference = float('inf')
    s1 = 0  # Initialize S_1 to 0
    # Loop from 1 to N-1 (1-indexed)
    for t in range(1, len(weights)):  # t corresponds to the division point (1-indexed)
        s1 += weights[t - 1]  # Access the weight using 0-indexing
        s2 = total_sum - s1  # Calculate S_2 based on the total sum
        difference = abs(s1 - s2)
        if difference < min_difference:
            min_difference = difference
    return min_difference
def main():
    """
    Main function to handle user input and output the minimum absolute difference.
    """
    try:
        n = int(input("Enter number of weights (N): "))
        if n <= 0:
            raise ValueError("N must be a positive integer.")
        weights_input = input("Enter weights separated by spaces: ").split()
        if len(weights_input) != n:
            raise ValueError("Number of weights does not match N.")
        # Validate that all weights are positive integers
        weights = []
        for weight in weights_input:
            weight_int = int(weight)  # Attempt to convert to integer
            if weight_int <= 0:
                raise ValueError("All weights must be positive integers.")
            weights.append(weight_int)
        min_difference = calculate_min_difference(weights)
        print(f"Minimum Absolute Difference: {min_difference}")
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()