'''
Main entry point of the application.
'''
from input_handler import InputHandler
from subsequence_calculator import SubsequenceCalculator
def main():
    input_handler = InputHandler()
    calculator = SubsequenceCalculator()
    # Read input values
    n = int(input("Enter N: "))
    d = int(input("Enter D: "))
    # Validate input for N and D
    if n <= 0:
        print("Invalid input. N must be a positive integer.")
        return
    sequence = input("Enter Sequence (space-separated): ").split()
    # Validate sequence length immediately after reading
    if len(sequence) != n:
        print(f"Invalid input. The sequence must contain exactly {n} elements.")
        return
    if input_handler.validate_input(n, d, sequence):
        result = calculator.longest_valid_subsequence(list(map(int, sequence)), d)
        print(f"The longest valid subsequence length is: {result}")
    else:
        print("Invalid input. Please check your sequence values.")
if __name__ == "__main__":
    main()