'''
Main application file for the sequence processing.
'''
from sequence_processor import insert_numbers
def main():
    input_sequence = input("Enter a sequence of integers (space-separated): ")
    try:
        # Split the input string into a list of integers
        sequence = list(map(int, input_sequence.split()))
        if not sequence:  # Check for empty input
            print("Input Error: Please enter a non-empty sequence of integers.")
            return
        result = insert_numbers(sequence)
        print("Processed Sequence:", ' '.join(map(str, result)))
    except ValueError:
        print("Input Error: Please enter valid integers.")
if __name__ == "__main__":
    main()