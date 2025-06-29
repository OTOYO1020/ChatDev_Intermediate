'''
Main application file for the valid sequence calculator.
'''
def validate_input(N, sequence):
    """
    Validate the input values.
    Args:
    N (int): The expected length of the sequence.
    sequence (list): The list of integers to validate.
    Returns:
    bool: True if valid, False otherwise.
    """
    if len(sequence) != N:
        print(f"Invalid input: Expected {N} integers, but got {len(sequence)}.")
        return False
    if any(x < 0 for x in sequence):
        print("Invalid input: Sequence elements must be non-negative integers.")
        return False
    return True
def main():
    while True:
        try:
            N = int(input("Enter the length of the sequence (N): "))
            if N <= 0:
                print("Invalid input: N must be a positive integer.")
                continue  # Prompt again for valid input
            sequence = list(map(int, input(f"Enter {N} integers separated by spaces: ").split()))
            # Validate the input sequence
            if not validate_input(N, sequence):
                continue  # Prompt again for valid input
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input: Please enter valid integers.")
    result = 1  # Initialize result to store the count of valid sequences
    MOD = 10**9 + 7  # Define the modulo constant
    # Iterate through each index to calculate valid choices
    for i in range(N):
        choices = sequence[i] - i  # Calculate valid choices for A[i]
        if choices <= 0:
            print(0)  # No valid sequences possible
            return
        result = (result * choices) % MOD  # Update result with modulo operation
    print(result)  # Output the final result
if __name__ == "__main__":
    main()