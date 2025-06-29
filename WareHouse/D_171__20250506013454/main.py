'''
Main entry point for the application that handles user interactions.
'''
from data_processor import DataProcessor
from input_handler import InputHandler
def main():
    input_handler = InputHandler()
    data_processor = DataProcessor()
    # Read integers N and Q from standard input
    N, Q = map(int, input("Enter N and Q (space-separated): ").strip().split())
    # Read the sequence A of length N from standard input
    sequence = list(map(int, input(f"Enter the sequence of length {N} (space-separated integers): ").strip().split()))
    data_processor.set_sequence(sequence)
    results = []
    # For each operation i from 1 to Q
    operations = input_handler.get_operations(Q)  # Get all operations at once
    for b, c in operations:
        sum_result = data_processor.replace_and_sum(b, c)  # Get the sum directly
        results.append(sum_result)  # Append the sum to results
    # Print each value in 'results' on a new line
    for result in results:
        print(result)
if __name__ == "__main__":
    main()